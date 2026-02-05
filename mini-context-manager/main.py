from contextlib import contextmanager

class HelloContextManager():
    def __enter__(self):
        print("entering context!")
        return "Enter function returns an object and binds it"
        
    def __exit__(self, exc_type, exc_value, exc_tb):
        print("leaving context now!")
        print(f"Exception: {exc_type} | {exc_value} | {exc_tb}")

@contextmanager
def write_file(file_path):
    try:
        file = open(file_path, mode='w')
        yield file
    finally:
        file.close()

def main():
    with HelloContextManager() as hello:
        print(hello)

    with write_file('new_file.txt') as file:
        for i in range(5):
            file.write(f'Round number: {i}\n')
    
main()