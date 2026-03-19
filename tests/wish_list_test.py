from playwright.sync_api import expect

from pages.wishlist_page import WishlistPage


def test_add_item_to_wish_list(page,logger,log_in_to_page):
    wish_list = WishlistPage(page,logger)
    wish_list.add_item_to_wishlist()
    expect(page.locator(wish_list.mac_book_link_in_wishlist_table)).to_be_visible()


def test_remove_item_from_wishlist(page,logger,log_in_to_page):
    wish_list = WishlistPage(page,logger)
    wish_list.add_item_to_wishlist()
    wish_list.remove_item_from_wishlist()
    expect(page.locator(wish_list.wish_list_empty_text)).to_be_visible()


def test_add_first_two_products_to_wish_list(page, logger, log_in_to_page):
    wish_list = WishlistPage(page, logger)
    products = wish_list.add_multiple_items_to_wishlist()

    assert len(products) >= 2
    expect(page.locator(f"//a[normalize-space()='{products[0]['name']}']")).to_be_visible()
    expect(page.locator(f"//a[normalize-space()='{products[1]['name']}']")).to_be_visible()
