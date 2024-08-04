from fastapi import APIRouter
import schemas.contact as contact_schema
from datetime import datetime
router = APIRouter()

@router.get("/contacts", response_model=list[contact_schema.Contact]) # 一覧表示
async def get_contacts():
    # モックデータ
    dummy_data = datetime.now()
    return [
        contact_schema.Contact(
            id=1,
            name="テスト太郎",
            email="test@test.com",
            url="http://test.com",
            gender=1,
            message="テストメッセージ",
            is_enabled=True,
            created_at=dummy_data,
        )
    ]

@router.post("/contacts", response_model=contact_schema.Contact) # 登録
async def create_contact(body: contact_schema.Contact):
    return contact_schema.Contact(**body.model_dump())
    

@router.get("/contacts/{contact_id}", response_model=contact_schema.Contact) # 詳細表示
async def get_contact(contact_id: int):
    return contact_schema.Contact(contact_id)

@router.put("/contacts/{contact_id}", response_model=contact_schema.Contact) # 更新
async def update_contact(contact_id: int, body: contact_schema.Contact):
    return contact_schema.Contact(**body.model_dump())


@router.delete("/contacts/{contact_id}", response_model=contact_schema.Contact) # 削除
async def delete_contact(contact_id: int):
    return