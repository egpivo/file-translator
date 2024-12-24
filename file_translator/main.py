import uvicorn
from fastapi import FastAPI
from routers.file_translate import router as file_translate_router

app = FastAPI()
app.include_router(file_translate_router)

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8009)
