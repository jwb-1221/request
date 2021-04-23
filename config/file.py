import os
from common import config

def cat_file():
    if os.path.exists(config.TEST_RESULT):  # 如果文件存在
        os.remove(config.TEST_RESULT)
    else:
        print("测试结果文件不存在")
    if os.path.exists(config.TEST_TOKEN):  # 如果文件存在
        os.remove(config.TEST_TOKEN)
    else:
        print("测试token文件不存在")
