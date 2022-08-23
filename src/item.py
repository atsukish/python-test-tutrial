"""itemクラス"""
from pydantic import BaseModel


class Item(BaseModel):

    """商品アイテム

    Args:
        name (str): 商品名
        price (float): 価格
        is_reduce_tax (bool): 軽減税率対象
    """

    name: str
    price: float
    is_reduce_tax: bool = False
