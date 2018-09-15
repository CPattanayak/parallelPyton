from multiprocessing import Pool
import os

def doubler(number):
    # if hasattr(os, 'getppid'):  # only available on Unix
    #     print('parent process:', os.getppid())
    print('process id:', os.getpid())
    return number * 2


if __name__ == '__main__':
    numbers = [5, 10, 20, 50, 60, 70]
    pool = Pool(processes=3)
    for i in numbers:
        result = pool.apply_async(doubler, (i,))
        print(result.get(timeout=1))