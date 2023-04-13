import os
from dotenv import load_dotenv
from fastapi import FastAPI
from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError

import uvicorn

from routes.api import router as api_router

# from commands import CreatePeopleCommand
# from entity import Person

# env load
load_dotenv(verbose=True)

app = FastAPI()

app.include_router(api_router)


@app.on_event("startup")
async def startup_event():
    # Kafka Admin Client
    client = KafkaAdminClient(bootstrap_servers=os.environ.get("BOOTSTRAP-SERVERS"))

    # topic config
    topic = NewTopic(
        name=os.environ.get("TOPIC_PEOPLE_BASIC_NAME"),
        num_partitions=int(os.environ.get("TOPIC_PEOPLE_BASIC_PARTITIONS")),
        replication_factor=int(os.environ.get("TOPIC_PEOPLE_BASIC_REPLICATION_FACTOR")),
    )

    try:
        client.create_topics([topic], validate_only=False)
    except TopicAlreadyExistsError as e:
        print(e)
    finally:
        client.close()


@app.get("/")
async def root():
    return {"message": "Kafka sample Project"}


if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info", reload="True")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    print("running")
