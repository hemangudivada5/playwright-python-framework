from pages.base_page import BasePage


class WishlistPage(BasePage):
    mac_book_item = "(//a[text()='MacBook'])[2]"
    wish_list_button = "//button[@data-original-title='Add to Wish List']"
    wish_list_link = "//a[@id='wishlist-total']"
    home_icon = "//a[text()='Qafox.com']"
    mac_book_link_in_wishlist_table = "//div[@id='content']//table[contains(@class,'table')]/tbody//a[normalize-space()='MacBook']"
    remove_icon_wishlist_page  = "(//button[@data-original-title='Add to Cart']/following::a)[1]"
    wish_list_empty_text = "//p[text()='Your wish list is empty.']"
    Desktop_dropdown_hover = "//a[@class='dropdown-toggle' and text()='Desktops']"
    showAll_desktops_option = "//a[text()='Show AllDesktops']"
    all_products = "//div[contains(@class,'product-layout')]"
    all_product_name_links = "//div[contains(@class,'product-layout')]//div[contains(@class,'caption')]/h4/a"
    product_page_wish_list_button = "(//button[@data-original-title='Add to Wish List'])[1]"

    def add_item_to_wishlist(self):
        self.click(self.home_icon)
        self.click(self.mac_book_item)
        self.click(self.wish_list_button)
        self.click(self.wish_list_link)

    def remove_item_from_wishlist(self):
        self.click(self.wish_list_link)
        self.click(self.remove_icon_wishlist_page)

    def add_multiple_items_to_wishlist(self):
        self.hover(self.Desktop_dropdown_hover)
        self.click(self.showAll_desktops_option)
        products = self.get_all_product_names_and_links()

        for product in products[:2]:
            self.logger.info(f"Opening product page for {product['name']}")
            self.page.goto(product["link"])
            self.click(self.product_page_wish_list_button)

        self.click(self.wish_list_link)
        return products

    def get_all_product_names_and_links(self):
        self.logger.info("Collecting all product names and links")
        product_elements = self.page.locator(self.all_product_name_links)
        product_count = product_elements.count()
        products = []

        for index in range(product_count):
            product = product_elements.nth(index)
            products.append({"name": product.text_content().strip(),"link": product.get_attribute("href"),})

        self.logger.info(f"Collected {product_count} products")
        return products
