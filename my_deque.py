from collections import deque

def is_palindrome(s):
    s = s.lower().replace(" ", "")

    char_queue = deque(s)

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    return True

if __name__ == "__main__":
    test_list = ['ioSoi', 'Lorem Ipsum dolor sit', 'Кабан упал и лапу набак']
    i = 0
    while i < len(test_list):
        print(f'{test_list[i]} -- {"is palindrome" if is_palindrome(test_list[i]) else "is not palindrome"}')
        i += 1
