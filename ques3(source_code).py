import psutil
import time
import threading # for multithreading

def find_usage(): #fuction to calculate usage for last 5 sec
    threading.Timer(5.0, find_usage).start()
    print "Current Usage"
    print psutil.cpu_percent()
    print psutil.virtual_memory()
    print psutil.disk_usage('/')

def find_usage_30sec(): #fuction to calculate usage for last 30 sec
    threading.Timer(30.0, find_usage_30sec).start()
    print "Usage in last 30 seconds"
    print psutil.cpu_percent()
    print psutil.virtual_memory()
    print psutil.disk_usage('/')

def find_usage_1min(): #fuction to calculate usage for last 1 min
    threading.Timer(60.0, find_usage_1min).start()
    print "Usage in last 1 minute"
    print psutil.cpu_percent()
    print psutil.virtual_memory()
    print psutil.disk_usage('/')

def find_usage_5min(): #fuction to calculate usage for last 5 min
    threading.Timer(300.0, find_usage_5min).start()
    print "Usage in last 5 minutes"
    print psutil.cpu_percent()
    print psutil.virtual_memory()
    print psutil.disk_usage('/')

find_usage()
find_usage_30sec()
find_usage_1min()
find_usage_5min()

import thread


thread.start_new_thread(find_usage,())
thread.start_new_thread(find_usage_30sec,())
thread.start_new_thread(find_usage_1min,())
thread.start_new_thread(find_usage_5min,())
