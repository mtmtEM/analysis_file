import json
import sys, os
from memory_profiler import profile

class ReadFiles:
    def __init__(self,path):
        self.path = path

    @profile
    def read_data(self):
        with open(self.path) as f:
            data = json.load(f)
            print(data)

if __name__ == '__main__':
    # path = '../files/sample.json'
    args = sys.argv

    if len(args) != 2:
        print("Incorrect args. ($ python3 main.py <File_path.json>)")
        sys.exit()
    elif os.path.exists(args[1]) == False:
        print("No such file or directory.")
        sys.exit()
    else:
        path = args[1]

    target = ReadFiles(path)
    target.read_data()
    print("fin.")
