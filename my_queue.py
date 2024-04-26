from queue import Queue
import random

queue = Queue()
id = 0

class Request:
    def __init__(self):
        global id
        id += 1
        self.id = id 

def generate_request():
    request = Request()
    queue.put(request)

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f'Заявка id:{request.id} успішно оброблена!')
    else:
        print("Заявок немає.")


if __name__ == "__main__":
    while True:
        generate_request()
        process_request()
