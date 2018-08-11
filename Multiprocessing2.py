import multiprocessing
import os

def worker(num):
    """thread worker function"""
    print ('Worker:', num)
    return

if __name__ == '__main__':
    jobs = []
    print(os.getenv('KEY_THAT_MIGHT_EXIST', "None123"))
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()