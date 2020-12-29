from fastapi import FastAPI
from loguru import logger
import uvicorn
import uuid

from tweebot_py.config import PROJECT_NAME, VERSION, LOG_LEVEL
from tweebot_py.service import load_model, generate, upload


app = FastAPI(title=PROJECT_NAME, version=VERSION)


@app.on_event("startup")
def startup_event():
    load_model()


@app.get("/health", tags=["sanity"])
def health():
    return {"status_code": 200, "response": "ok"}


@app.get(
    "/tweets", tags=["services"], summary="Generates bunch of tweets",
)
async def tweets():
    """Generate tweets and upload them to environment user drafts"""
    with logger.contextualize(request_id=str(uuid.uuid4())):
        tweets = generate()
        upload(tweets)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=80, log_level=LOG_LEVEL)