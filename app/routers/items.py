from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.crud.item import (
    create_item,
    delete_item,
    get_item,
    get_items,
    update_item,
)
from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate

router = APIRouter(prefix="/items", tags=["Items"])


@router.post("", response_model=ItemResponse)
def create(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db, item)


@router.get("", response_model=List[ItemResponse])
def read_all(db: Session = Depends(get_db)):
    return get_items(db)


@router.get("/{item_id}", response_model=ItemResponse)
def read_one(item_id: int, db: Session = Depends(get_db)):
    item = get_item(db, item_id)

    if item is None:
        raise HTTPException(status_code=404, detail="Item non trouvé")

    return item


@router.put("/{item_id}", response_model=ItemResponse)
def update(
    item_id: int,
    item_update: ItemUpdate,
    db: Session = Depends(get_db),
):
    item = update_item(db, item_id, item_update)

    if item is None:
        raise HTTPException(status_code=404, detail="Item non trouvé")

    return item


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    item = delete_item(db, item_id)

    if item is None:
        raise HTTPException(status_code=404, detail="Item non trouvé")

    return {"message": "Item supprimé avec succès"}