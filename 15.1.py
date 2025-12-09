#import
import multiprocessing
import time
import random
from datetime import datetime

def process():
    #add sleep time
    sleeper = random.uniform(0, 1)
    time.sleep(sleeper)
    
    #print time
    print(f"Process {multiprocessing.current_process().name}: Current time is {datetime.now()}")

if __name__ == "__main__":
    
    processes = []
    
    for i in range(3):
        #target the process function
        p = multiprocessing.Process(target=process, name=f"Process-{i+1}")
        #add process
        processes.append(p)
        p.start()  # Start the process

    for p in processes:#complete the process
        p.join()