import json

class ReadFiles:
    def __init__(self,path):
        self.path = path

    def read_data(self):
        with open(self.path) as f:
            data = json.load(f)
            print(data)

if __name__ == '__main__':
    print("<start>")
    path = '../files/sample.json'
    target = ReadFiles(path)
    target.read_data()
    print("<fin.>")
