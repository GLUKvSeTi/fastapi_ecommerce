from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, update
from starlette import status
from sqlalchemy.ext.asyncio import AsyncSession

from app.backend.db_depends import get_db
from ..models.review import Review

router = APIRouter(prefix='/reviews', tags=['reviews'])

@router.get('/all_reviews')
async def all_reviews(db: Annotated[AsyncSession, Depends(get_db)]):
    reviews = await db.scalars(select(Review).where(Review.is_active == True))
    if not reviews:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='There are no review')
    return reviews

@router.get('/products_reviews/{product_id}')
async def product_reviews(db: Annotated[AsyncSession, Depends(get_db)], product_id: int):
    reviews = await db.scalars(select(Review).where(Review.id == product_id, Review.is_active == True))
    if not reviews:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='There are no review')
    return reviews

