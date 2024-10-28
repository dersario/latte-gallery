from fastapi import APIRouter,status
from latte_gallery.schemas import *

router = APIRouter(prefix="/get", tags=["Статус"])
accounts_router = APIRouter(prefix="/accounts", tags=["Аккаунты"])
pictures_router = APIRouter(prefix="/pictures", tags=["Картинки"])
@router.get("/status", summary="Получить статус сервера")
def get_status() -> StatusResponse:
    return StatusResponse(status="ok")

@accounts_router.post('/register', summary="Регистрация нового аккаунта", status_code=status.HTTP_201_CREATED)
def register(body: AccountRegister) -> Account:
    return Account(
        id = 1,
        login = body.login,
        name = body.name,
        role = Role.USER,
    )

@accounts_router.get('/my', summary="Получение данных аккаунта", status_code=status.HTTP_201_CREATED)
def register() -> Account:
    return Account(
        id = 1,
        login = "абстрактный Пася",
        name = "Пася",
        role = Role.USER,
    )

@accounts_router.get('', summary="Получение списка всех аккаунтов", status_code=status.HTTP_201_CREATED)
def get_accounts(page: int = 0, size: int = 10) -> GetAccounts:
    return GetAccounts(
        count = 1,
        items = [
            {
                "id": 1,
                "login": "user1",
                "name": "Василий Пупкин",
                "role": "USER"
            }
        ]
    )

@accounts_router.get("/{id}", summary="Получение аккаунта по идентификатору", status_code=status.HTTP_201_CREATED)
def get_account(id) -> Account:
    return Account(
        id=id,
        login="PasVupkin228",
        name="Пася Вупкин",
        role=Role.USER
    )

@router.get("/kok", summary="Получить кок")
def get_kok() -> KokResponse:
    return KokResponse(kok="kok")

@pictures_router.post("", summary="Создать новую картинку")
def create_picture() -> CreatePicture:
    return CreatePicture(
        {
            "title": "Котик",
            "tags": [
                "cats",
                "adorable",
                "cute"
            ],
            "is_private": False,
            "file_uuid": "9affceb3-d9ef-4a2f-9ec2-0932c56b8648"
        }
    )

@pictures_router.get("", summary="Получить список всех")
def get_pictures(page: int = 0, size: int=10, title: str = "title", owner_id: str="owner_id", tags = list[str]) -> GetPictures:
    return GetPictures(
        count = 10,
        items = [
            {
            "id": 1,
            "title": "Котик",
            "creation_date_time": "2024-10-28T15:57:49.956Z",
            "tags": [
                "cats",
                "adorable",
                "cute"
            ],
            "is_private": False,
            "owner_id": 1,
            "file_uuid": "9affceb3-d9ef-4a2f-9ec2-0932c56b8648"
            }
        ]
    )