from typing import Union

from .api.social.router import social_router

from fastapi import FastAPI

app = FastAPI()
app.include_router(social_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
