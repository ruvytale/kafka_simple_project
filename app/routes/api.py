from fastapi import APIRouter
from src.endpoints import kafka_producer

router = APIRouter()
router.include_router(kafka_producer.router)
