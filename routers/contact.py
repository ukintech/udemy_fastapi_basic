from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import schemas.contact as contact_schema
import cruds.contact as contact_cruds
from database import get_db
from datetime import datetime
router = APIRouter()

@router.get("/contacts", response_model=list[contact_schema.ContactList]) # 一覧表示
async def get_contacts(db: AsyncSession = Depends(get_db)):
    # モックデータ
    dummy_data = datetime.now()
    return await contact_cruds.get_contacts_all(db)

@router.post("/contacts", response_model=contact_schema.ContactCreate) # 登録
async def create_contact(body: contact_schema.ContactCreate, db: AsyncSession = Depends(get_db)):
    return await contact_cruds.create_contact(db, body)
    

@router.get("/contacts/{contact_id}", response_model=contact_schema.ContactDetail) # 詳細表示
async def get_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    contact = await contact_cruds.get_contact(db, contact_id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@router.put("/contacts/{contact_id}", response_model=contact_schema.ContactCreate) # 更新
async def update_contact(contact_id: int, body: contact_schema.ContactCreate, db: AsyncSession = Depends(get_db)):
    contact = await contact_cruds.get_contact(db, contact_id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return await contact_cruds.update_contact(db, body, original=contact)


@router.delete("/contacts/{contact_id}", response_model=None) # 削除
async def delete_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    contact = await contact_cruds.get_contact(db, contact_id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return await contact_cruds.delete_contact(db, contact)



def get_message():
    message = "Hello, World!"
    print(f"message: {message}")
    return message

@router.get("/depends")
async def main(message: str = Depends(get_message)):
    print(f"エンドポイント: {message}")
    return {"message": message}