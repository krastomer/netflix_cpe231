from app.dependencies import get_current_user, get_storage
from fastapi import APIRouter, Depends
from database.schemas import UserHash

router = APIRouter(
    prefix='/poster',
    tags=['poster'],
    responses={404: {'description': 'Not found'}}
)


# @router.get('/')
# async def get_poster_all(movie: str = None, user: UserHash = Depends(get_current_user)):
#     if movie == None:
#         raise
#     storage = await get_storage()
#     list_url = []
#     count = 0
#     for i in storage.child().list_files():
#         if i.name.startswith('poster/' + movie) and i.name.endswith('.jpg'):
#             list_url.append({count: storage.child(i.name).get_url('')})
#             count += 1
#     if count == 0:
#         raise notfound_exception
#     return {movie: list_url}

# edit schema and add function for security data
