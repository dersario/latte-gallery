from fastapi import APIRouter,status
from latte_gallery.schemas import StatusResponse, KokResponse, AccountRegister, Account, Role

router = APIRouter(prefix="/get")
accounts_router = APIRouter(prefix="/accounts", tags=["Аккаунты"])
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

@router.get("/kok", summary="Получить кок")
def get_kok() -> KokResponse:
    return KokResponse(kok="kok")