import subprocess

# Run the service corresponding to the user_app
def run_user_service():
    subprocess.Popen(["D:\\version_1_social_media_app\\version_1\\venv\Scripts\\python.exe", "user_app/app.py"])

# Run the service corresponding to the post_app
def run_post_service():
    subprocess.Popen(["D:\\version_1_social_media_app\\version_1\\venv\\Scripts\\python.exe", "post_app/app.py"])

if __name__ == '__main__':
    run_user_service()
    run_post_service()

    # Graceful Termination of the two subprocesses
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nTerminating both the processes. Alvida!")
