# 多线程创建

import threading


def print_thread_names():
    print('Current thread name:', threading.current_thread().name)



threads = []
for i in range(8):
    thread = threading.Thread(target=print_thread_names)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

