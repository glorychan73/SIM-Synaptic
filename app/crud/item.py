from sqlalchemy.orm import Session

from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate


def create_item(db: Session, item: ItemCreate):
    new_item = Item(
        name=item.name,
        description=item.description,
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item


def get_items(db: Session):
    return db.query(Item).all()


def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()


def update_item(db: Session, item_id: int, item_update: ItemUpdate):
    item = get_item(db, item_id)

    if item is None:
        return None

    item.name = item_update.name
    item.description = item_update.description

    db.commit()
    db.refresh(item)

    return item


def delete_item(db: Session, item_id: int):
    item = get_item(db, item_id)

    if item is None:
        return None

    db.delete(item)
    db.commit()

    return item
