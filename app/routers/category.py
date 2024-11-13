from fastapi import APIRouter

router = APIRouter(prefix='/category', tags=['category'])


@router.get('/')
async def get_all_categories():
    pass

@router.post('/')
async def create_category():
    pass

@router.put('/{category_id}')
async def update_category(category_id: int):
    pass

@router.delete('/{category_id}')
async def delete_category(category_id: int):
    pass