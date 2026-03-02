from pages.base_page import BasePage


class WishlistPage(BasePage):
    mac_book_item = "(//a[text()='MacBook'])[2]"
    wish_list_button = "//button[@data-original-title='Add to Wish List']"
    wish_list_link = "//a[@id='wishlist-total']"
    home_icon = "//a[text()='Qafox.com']"
    mac_book_link_in_wishlist_table = "//div[@id='content']//table[contains(@class,'table')]/tbody//a[normalize-space()='MacBook']"

    def add_item_to_wishlist(self):
        self.click(self.home_icon)
        self.click(self.mac_book_item)
        self.click(self.wish_list_button)
        self.click(self.wish_list_link)
