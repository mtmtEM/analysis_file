import json, sys, os, ast
import sql
from time import sleep
from memory_profiler import profile

class ReadFiles:
    def __init__(self, path, dbname):
        self.path = path
        self.db = dbname

    # @profile
    def read_data(self):
        db = sql.DBconnect(self.db)
        db.creat_database()
        db.delete_database()
        id = 1
        with open(self.path, 'r', encoding='utf-8') as f:
            for line in f:
                # 初期化
                logs = []
                line = line.replace("\\n", "").replace("\\", "")
                # str -> dict 変換
                data = ast.literal_eval(line)

                logs.append(id)
                logs.append(data["eventid"])
                logs.append(data["ttylog"])
                logs.append(data["timestamp"])
                logs.append(data["message"])
                logs.append(data["isError"])
                logs.append(data["src_ip"])
                logs.append(data["session"])
                logs.append(data["sensor"])

                db.update_database(logs)
                id += 1

        db.show_database()

if __name__ == '__main__':
    args = sys.argv

    # $ python main.py ../logs/sample.json ../db/sample.db
    if len(args) != 3:
        print("Incorrect args. ($ python3 main.py <File_path.json> <DBname>)")
        sys.exit()
    elif os.path.exists(args[1]) == False:
        print("No such file or directory.")
        sys.exit()
    else:
        path = args[1]
        dbname = args[2]

    target = ReadFiles(path, dbname)
    target.read_data()

    print("fin.")
