import time

def monitor_log_file(filename, check_interval=10):
    with open(filename, 'r') as f:
        expected = f.read()  # Store the initial state

    while True:
        time.sleep(check_interval)  # Wait for the specified interval
        with open(filename, 'r') as f:
            new_contents = f.read()

        if expected != new_contents:
            raise RuntimeError("Warning! The log file has been changed.")

        print("The log file is unchanged.")  # Optional: Log the status

# Start monitoring with a 10-second interval
monitor_log_file('log.txt', check_interval=0.5)
