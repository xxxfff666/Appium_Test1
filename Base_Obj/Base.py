from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def find_elements(self, loc, timeout=20, poll=0.5):
        # 定位一组元素
        return WebDriverWait(self.driver, timeout, poll) \
            .until(lambda x: x.find_elements(*loc))

    def find_element(self, loc, timeout=10, poll=0.5):
        """
        :param loc: 元组 例如：（By.XPATH, "XPATH语句"）
        :param timeout:
        :param poll:
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll)\
            .until(lambda x: x.find_element(*loc))

    def click_element(self, loc):
        # 点击元素
        self.find_element(loc).click()

    def input_element(self, loc, text):
        # 输入元素
        input = self.find_element(loc)
        input.clear()
        input.send_keys(text)