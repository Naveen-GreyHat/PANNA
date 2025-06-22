import os

def simulate_shutdown():
    # Send SIGTERM to all processes (asking them to exit)
    for pid in os.popen("ps -ef").read().splitlines():
        try:
            os.kill(int(pid.split()[1]), signal.SIGTERM)
        except OSError as e:
            print(f"Error sending SIGTERM to process {pid}: {e}")

    # Wait for all processes to exit
    while True:
        try:
            os.waitpid(-1, 0)  # Wait for any child process to finish
        except ChildProcessError:
            pass

    print("Simulation of system shutdown complete!")
