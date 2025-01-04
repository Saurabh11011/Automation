import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
    return(seconds)
# t1 = time.perf_counter()
# # func(2)
# # func(4)
# # func(6)
# thread1 = threading.Thread(target=func,args=[2])
# thread2 = threading.Thread(target=func,args=[4])
# thread3 = threading.Thread(target=func,args=[6])
# thread1.start()
# thread2.start()
# thread3.start()
# thread1.join()
# thread2.join()
# thread3.join()
# t2 = time.perf_counter()
# print(f"time taken by the script = {t2-t1}")

def multi():
   t1 = time.perf_counter()
   with ThreadPoolExecutor() as executor:
       future1 = executor.submit(func,3)
       future2 = executor.submit(func,5)
       future3 = executor.submit(func,6)
       print(future2.result())
       print(future3.result())
       print(future1.result())
   t2 = time.perf_counter()
   print(f"time taken by it is = {t2-t1}")
multi()
