import uvicorn
from fastapi import FastAPI

from exceptions import StartHoursException
from pydantic_schemas import UsersData

from redis_conn_methods.methods import write_data, check_data

app = FastAPI(
    title="Тестовое задание"
)


@app.post("/write_data", tags=['запись и обновление данных'])
async def write_data_endpoint(data: UsersData):
    await write_data(data.phone, data.address)
    return {"message": f"Данные для номера телефона {data.phone} были записаны или обновлены."}


@app.get("/check_data", tags=['получение данных'])
async def check_data_endpoint(phone: str):
    address = await check_data(phone)
    if not address:
        raise StartHoursException()
    return {"address": address}


# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True)
