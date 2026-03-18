from pages.base_page import BasePage


class WishlistPage(BasePage):
    mac_book_item = "(//a[text()='MacBook'])[2]"
    wish_list_button = "//button[@data-original-title='Add to Wish List']"
    wish_list_link = "//a[@id='wishlist-total']"
    home_icon = "//a[text()='Qafox.com']"
    mac_book_link_in_wishlist_table = "//div[@id='content']//table[contains(@class,'table')]/tbody//a[normalize-space()='MacBook']"
    remove_icon_wishlist_page  = "(//button[@data-original-title='Add to Cart']/following::a)[1]"
    wish_list_empty_text = "//p[text()='Your wish list is empty.']"

    def add_item_to_wishlist(self):
        self.click(self.home_icon)
        self.click(self.mac_book_item)
        self.click(self.wish_list_button)
        self.click(self.wish_list_link)

    def remove_item_from_wishlist(self):
        self.click(self.wish_list_link)
        self.click(self.remove_icon_wishlist_page)
