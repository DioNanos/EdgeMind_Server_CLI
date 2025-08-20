import os
import subprocess
import uuid
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory store for active subprocesses.
# NOTE: This is a simple implementation. For production, you might want a more
# robust session management that can handle server restarts.
sessions = {}

# Get the secret API key from an environment variable.
SECRET_API_KEY = os.environ.get("API_KEY")
if not SECRET_API_KEY:
    raise ValueError("No API_KEY environment variable set for the application.")

@app.before_request
def check_api_key():
    """Checks for a valid API key in the Authorization header before each request."""
    if request.path == '/health': # Allow health checks without a key
        return

    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({"error": "Authorization header is missing"}), 401
    
    parts = auth_header.split()

    if parts[0].lower() != 'bearer' or len(parts) != 2:
        return jsonify({"error": "Invalid Authorization header format. Expected 'Bearer <token>'"}), 401
    
    token = parts[1]
    if token != SECRET_API_KEY:
        return jsonify({"error": "Invalid API Key"}), 403 # 403 Forbidden is more appropriate here

@app.route('/health', methods=['GET'])
def health_check():
    """A simple health check endpoint."""
    return jsonify({"status": "ok"}), 200

@app.route('/execute', methods=['POST'])
def execute():
    """
    Executes a command in a persistent subprocess session.
    """
    data = request.json
    session_id = data.get('session_id')
    profile = data.get('profile')
    cwd = data.get('cwd', '/')
    user_input = data.get('input', '') + '\n' # Ensure newline for CLI tools

    if not profile or not profile.get('executable_path'):
         return jsonify({"error": "Invalid profile configuration in request"}), 400

    # If session_id is not provided or not found, start a new session.
    if not session_id or session_id not in sessions:
        session_id = str(uuid.uuid4())
        
        command = [profile['executable_path']]
        if profile.get('chat_subcommand'):
            command.append(profile['chat_subcommand'])
        if profile.get('startup_args'):
            command.extend(profile['startup_args'].split())

        try:
            if not os.path.isdir(cwd):
                return jsonify({"error": f"Working directory not found: {cwd}"}), 400

            # Start the subprocess
            process = subprocess.Popen(
                command,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=cwd,
                bufsize=1, # Line-buffered
                universal_newlines=True
            )
            sessions[session_id] = process
        except Exception as e:
            return jsonify({"error": f"Failed to start process: {str(e)}"}), 500

    process = sessions.get(session_id)
    if process.poll() is not None: # Check if the process has terminated
        del sessions[session_id]
        return jsonify({"error": "Process terminated unexpectedly. Starting a new session might be required."}), 500

    try:
        # Write user input to the process's stdin
        process.stdin.write(user_input)
        process.stdin.flush()
        
        # Read the response from stdout.
        # This is a simplified readline(). For tools with multi-line outputs
        # that don't flush on each line, a more complex async reading
        # mechanism would be needed.
        output = process.stdout.readline()

    except BrokenPipeError:
        # This happens if the process terminates after we check poll() but before we write.
        del sessions[session_id]
        return jsonify({"error": "Process pipe was broken. The process may have terminated."}), 500
    except Exception as e:
        return jsonify({"error": f"An error occurred while communicating with the process: {str(e)}"}), 500

    # For now, we are not capturing stderr separately, but it could be added.
    return jsonify({
        "session_id": session_id,
        "output": output.strip(),
        "error": "" # Simplified
    })

if __name__ == '__main__':
    # This block is for direct execution, not used when running with `flask run`
    # The host and port are configured via environment variables for Flask
    app.run()
