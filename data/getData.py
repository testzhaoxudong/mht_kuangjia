import csv
import os

def getdata(file_path,line):
    # base_dir=os.path.dirname(__file__)
    # file_path=os.path.join(base_dir,"denglu.csv")
    with open(file_path,'r',encoding='utf-8') as mht_data:
        data=csv.reader(mht_data)
        list_data=list(data)
    # print(list_data)
    return list_data[line-1]

if __name__ == '__main__':
    print(getdata("../data/denglu.csv",2))
