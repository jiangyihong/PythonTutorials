from multiprocessing import Process
import os


def run_child_process(name):
    print("Child process is start %s (%s)" % (name, os.getpid()))


if __name__ == '__main__':
    print("Parent process is %s" % os.getpid())
    # 创建子进程
    child_process = Process(target=run_child_process, args=('test',))
    print('Child process will start')
    # 启动子进程
    child_process.start()
    # 等待子进程结束
    child_process.join()
    print('Child process end.')
