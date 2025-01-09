import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class RunScriptHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("runstock.py"):
            subprocess.run(["python", "runstock.py"])

if __name__ == "__main__":
    path = "."
    event_handler = RunScriptHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()