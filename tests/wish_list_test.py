from playwright.sync_api import expect

from pages.wishlist_page import WishlistPage


def test_add_item_to_wish_list(page,logger,log_in_to_page):
    wish_list = WishlistPage(page,logger)
    wish_list.add_item_to_wishlist()
    expect(page.locator(wish_list.mac_book_link_in_wishlist_table)).to_be_visible()
