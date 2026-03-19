class BasePage:
    def __init__(self,page,logger):
        self.page = page
        self.logger = logger

    def click(self,locator):
        self.logger.info(f"clicking {locator}")
        self.page.locator(locator).click()

    def fill(self,locator,value):
        self.logger.info(f"filling {locator}")
        self.page.locator(locator).fill(value)

    def get_text(self,locator):
        self.logger.info(f"getting text {locator}")
        return self.page.locator(locator).text_content()

    def hover(self, locator):
        self.logger.info(f"hovering on {locator}")
        self.page.locator(locator).hover()

    def hover(self, locator):
        self.logger.info(f"hovering on {locator}")
        self.page.locator(locator).hover()
