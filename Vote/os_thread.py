# _*_ coding:utf-8 _*_
import os
import time
from concurrent.futures import ThreadPoolExecutor

def task():
    command=" python index.py "
    os.system(command)
def main():
    pool=ThreadPoolExecutor(5)
    task_count=1000
    for i in range(0,task_count):
        print("第%d次"%i)
        pool.submit(task)
        time.sleep(3)
    pool.shutdown()
if __name__ == '__main__':
    main()