import os
import shutil
import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="C:/Users/infos/Downloads"

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Connection: {event}")

event_handler=MyHandler()
observer=Observer()
observer.schedule(event_handler, from_dir, recursive=True)
#observer.schedule({Class object}, {Where directory}, {Checks all subdirectories if true})
observer.start()

while True:
    time.sleep(2)
    print("running...")
