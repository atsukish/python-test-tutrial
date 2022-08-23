"""item.pyテスト"""
from src.item import Item


def test_item() -> None:

    item1 = Item(name="ice cream", price=100, is_reduce_tax=True)
    assert item1.name == "ice cream"
    assert item1.price == 100
    assert item1.is_reduce_tax

    item2 = Item(name="beer", price=180, is_reduce_tax=False)
    assert item2.name == "beer"
    assert item2.price == 180
    assert not item2.is_reduce_tax
