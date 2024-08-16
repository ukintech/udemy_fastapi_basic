from typing import List, Tuple
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
import schemas.contact as contact_schema
import models.contact as contact_model
from datetime import datetime

async def create_contact(db: AsyncSession, contact: contact_schema.ContactCreate) -> contact_model.Contact:
    """
    DBに保存
    
    Args:
        db (AsyncSession): DBセッション
        contact (ContactCreate): 保存するデータ
    
    Returns:
        Contact: 保存したデータ
    """
    contact_data = contact.model_dump()
    if contact_data["url"] is not None:
        contact_data["url"] = str(contact_data["url"])

    db_contact = contact_model.Contact(**contact_data)
    db.add(db_contact) # 保存
    await db.commit() # コミット
    await db.refresh(db_contact) # リフレッシュ
    return db_contact

async def get_contacts_all(db: AsyncSession) -> List[Tuple[int, str, datetime]]:
    """
    全件取得
    
    Args:
        db (AsyncSession): DBセッション
    
    Returns:
        List[Contact]: 取得したデータ
    """
    result: Result = await db.execute(select(contact_model.Contact.id, contact_model.Contact.name, contact_model.Contact.created_at))
    return result.all()

async def get_contact(db: AsyncSession, contact_id: int) -> contact_model.Contact | None:
    """
    1件取得
    
    Args:
        db (AsyncSession): DBセッション
        contact_id (int): 取得するID
    
    Returns:
        Contact: 取得したデータ
    """
    query = select(contact_model.Contact).where(contact_model.Contact.id == contact_id)
    result: Result = await db.execute(query)
    return result.scalars().first()

async def update_contact(db: AsyncSession, contact: contact_schema.ContactCreate, original: contact_model.Contact) -> contact_model.Contact:
    """
    更新
    
    Args:
        db (AsyncSession): DBセッション
        contact (ContactCreate): 更新するデータ
        original (Contact): 更新前のデータ
    
    Returns:
        Contact: 更新したデータ
    """
    original.name = contact.name
    original.email = contact.email
    if original.url is not None:
        original.url = str(contact.url)
    original.gender = contact.gender
    original.message = contact.message
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original

async def delete_contact(db: AsyncSession, original: contact_model.Contact) -> None:
    """
    削除
    
    Args:
        db (AsyncSession): DBセッション
        original (Contact): 削除するデータ
    """
    await db.delete(original)
    await db.commit()
    return