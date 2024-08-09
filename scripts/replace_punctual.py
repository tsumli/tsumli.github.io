import shutil
import datetime
import os, sys
import glob
import re


post_ls = glob.glob("/workdir/content/**/main.md", recursive=True)
print(post_ls)
pattern = re.compile('[^\u3041-\u309F\s\w]\$[\\\\\d\s\w^\$]+\$[^\u3041-\u309F\s\w]')
for file_name in post_ls:
    print(file_name)
    with open(file_name, "r") as f:
        data = f.read()
    # data = data.replace("、", "，").replace("。", "．")
    res = re.findall(pattern, data)
    print(res)
    with open(file_name, "w") as f:
        f.write(data)
    sys.exit()