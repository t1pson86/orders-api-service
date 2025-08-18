import uvicorn
from fastapi import FastAPI
from faststream.rabbit.fastapi import RabbitRouter

app = FastAPI()
router = RabbitRouter()


@router.post("/order")
async def create_order(name: str):
    await router.broker.publish(
        f"Новый заказ: {name}",
        queue="orders"
    )
    return {"data": "ok"}


app.include_router(router)
