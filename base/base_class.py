class Base:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Current URL print"""
        url = self.driver.current_url
        print(f'Current URL: {url}')

    def assert_url(self, result):
        """Checking URL"""
        url = self.driver.current_url
        assert url == result
        print('Correct URL')

    def assert_word(self, word, result):
        """Checking word"""
        value_word = word.text
        assert value_word == result
        print('Correct value')

