from fastapi import FastAPI
from controller.controller import router as sesion_router

app = FastAPI(title="Liga de Fútbol API")

app.include_router(sesion_router, prefix="/api/v1", tags=["liga"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)