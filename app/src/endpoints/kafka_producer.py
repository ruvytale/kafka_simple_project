# environment
import os
from dotenv import load_dotenv

# api
from fastapi import APIRouter
from fastapi import Query

# src
from src.models.commands import CreatePeopleCommand
from src.models.person import Person
from src.utils.kafka import make_producer

# util
import uuid
from typing import Optional
from typing import List
from faker import Faker

router = APIRouter(
    prefix="/api",
    tags=["kafka"],
    responses={404: {"description": "Not Found"}},
)


@router.post("/people", status_code=201, response_model=List[Person])
async def create_people(cmd: CreatePeopleCommand):
    people: List[Person] = []

    faker = Faker()

    producer = make_producer()

    for _ in range(cmd.count):
        person = Person(
            id=str(uuid.uuid4()), title=faker.job(), name=faker.name(), email=faker.email()
        )
        print(person)

        people.append(person)
        producer.send(
            topic=os.environ.get("TOPIC_PEOPLE_BASIC_NAME"),
            key=person.title.lower().replace(r"s+", "-").encode("utf-8"),
            value=person.json().encode("utf-8"),
        )

    producer.flush()

    return people
