from multiprocessing import Pool
import os


def run_child_process(name_list):
    print('The child process pid is %s ' % os.getpid())
    for name in name_list:
        print(name)


if __name__ == '__main__':
    print('Parent process pid is %s ' % os.getpid())
    names = ['张三', '李四', '王五', '赵六']
    # 创建进程池
    pool = Pool()
    for i in range(5):
        pool.apply_async(run_child_process, args=(names,))
    # 启动进程池
    pool.close()
    pool.join()
    print('All subprocess done.')
