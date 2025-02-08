import time

class LogMonitor:
    def __init__(self, filename, check_interval=0.5):
        self.filename = filename
        self.check_interval = check_interval
        self.expected = self._read_file()

    def _read_file(self):
        with open(self.filename, 'r') as f:
            return f.read()

    def start_monitoring(self):
        print(f"Monitoring {self.filename} for changes...")
        while True:
            time.sleep(self.check_interval)
            new_contents = self._read_file()
            if self.expected != new_contents:
                raise RuntimeError("Warning! The log file has been changed.")
            print("The log file is unchanged.")

# Example usage
if __name__ == "__main__":
    monitor = LogMonitor('log.txt', check_interval=0.5)
    monitor.start_monitoring()