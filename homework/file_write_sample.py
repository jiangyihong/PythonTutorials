#!/usr/bin/python
# -*- coding: UTF-8 -*-
import  json


# 打开文件
json_data = json.dumps({"title":"中文"}, ensure_ascii=False, indent=2)
filename = "test.txt"
with open(filename, "w",encoding="utf8") as file_object:
    file_object.write(json_data)
