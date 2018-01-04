from multiprocessing import Process
import os


def run_child_process(name):
    print("Child process pid is %s and %s" % (os.getpid(), name))


if __name__ == "__main__":
    print("Parent process pid is %s " % os.getpid())
    # 创建子进程
    child_process = Process(target=run_child_process, args=('test',))
    print('Child process will start')
    child_process.start()
    child_process.join()
    print("Child process end")
