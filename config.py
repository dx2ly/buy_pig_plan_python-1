from selenium import webdriver


target = {
    "phone": "13357969456",
    "name": "小明",
    "email": "896519741@qq.com",
    "address": "这个男人来自地球",
    "comment": "谢谢！不会～"
}

settings = {
    "times": 100,
    "timeout": 5,
    "driver":webdriver.Firefox(),
}
