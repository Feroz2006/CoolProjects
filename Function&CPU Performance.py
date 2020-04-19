from time import time

def performance(function):
  def wrapper(*args, **kwargs):
    t1 = time()
    result = function(*args, **kwargs)
    t2 = time()
    print(f"It took {t2-t1} seconds for your computer to do this function.")
    return result
  
  return wrapper


@performance
def run_time():
  for i in range(100000000):
    i *= 5

run_time()