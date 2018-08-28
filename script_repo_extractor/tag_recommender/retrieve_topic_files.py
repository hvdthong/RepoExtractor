from os import listdir
from os.path import isfile, join
import json
from extract_tag_url import load_file
import os


def write_file(path_file, data):
    split_path = path_file.split("/")
    path_ = split_path[:len(split_path) - 1]
    path_ = "/".join(path_)

    if not os.path.exists(path_):
        os.makedirs(path_)
    with open(path_file, 'w') as out_file:
        for line in data:
            # write line to output file
            out_file.write(str(line))
            out_file.write("\n")
        out_file.close()


if __name__ == "__main__":
    print 'hello'
    exit()
    path_ = "./output_url_json/"
    onlyfiles = [f for f in listdir(path_) if isfile(join(path_, f))]
    data_ = list()
    for f in onlyfiles:
        # print load_file(path=path_ + f)[0]
        json_file = json.loads(load_file(path=path_ + f)[0])
        # print json_file["topics"]
        if len(json_file["topics"]) != 0:
            topics = [t for t in json_file["topics"]]
            print f + "\t" + ":".join(topics)
            data_.append(f + "\t" + ":".join(topics))
    write_file(path_file="./Topics_Projects.txt", data=data_)
