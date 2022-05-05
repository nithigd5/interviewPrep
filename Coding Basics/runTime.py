import time

def dispRunTime(fun):
    def run(*args):
        start = time.time()
        fun(*args)
        end = time.time()
        print((end - start)," seconds")
    return run

def runTime(fun, *args):
    start  = time.time()
    r = fun(*args)
    end = time.time()
    print(end - start, " Seconds")
    return r