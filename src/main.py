"""main.py"""
from http import HTTPStatus

from fastapi import FastAPI

from src.item import Item

app = FastAPI()


@app.get("/health", status_code=HTTPStatus.OK)
async def health() -> dict:
    """ヘルスチェックAPI

    Returns:
        dict: API実行結果
    """
    return {"health": "OK"}


@app.post("/tax_price")
async def price(item: Item) -> dict:
    """税込み価格

    Args:
        item (Item): 商品アイテム

    Returns:
        int: 税込価格
    """
    if item.is_reduce_tax:
        return {"price_with_tax": int(item.price * 1.08)}
    else:
        return {"price_with_tax": int(item.price * 1.1)}
