import pytest
import allure
from pages.inventory_page import InventoryPage
from playwright.sync_api import expect


def test_inventory_page_elements(page,setup_inventory):

    inventory = InventoryPage(page)
    inventory.add_item_to_cart("Sauce Labs Onesie")
    inventory.add_item_to_cart("Test.allTheThings() T-Shirt (Red)")
    assert int(inventory.get_total_items_in_cart()) == 2
          

