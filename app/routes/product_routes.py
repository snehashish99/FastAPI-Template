from fastapi import APIRouter


router = APIRouter()


@router.get("/products")
async def get_products():
    return {"message": "List of products"}


@router.post("/products")
async def create_product():
    return {"message": "Product created"}
