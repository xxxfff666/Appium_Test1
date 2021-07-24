from appium import webdriver

"""
    搜索
"""
def init_driver_search():
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6.0'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app信息
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'
    # 中文输入允许
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 声明driver对象
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    return driver

"""
    发送短信
"""
def init_driver_send():
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6.0'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app信息
    desired_caps['appPackage'] = 'com.android.messaging'
    desired_caps['appActivity'] = '.ui.conversationlist.ConversationListActivity'
    # 中文输入允许
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 声明driver对象
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    return driver