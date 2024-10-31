# import uvicorn
# from fastapi import FastAPI

# from app.apis.routes import services

# app = FastAPI(title="Parkway")

# app.include_router(services.router)

# if __name__ == "__main__":
#    uvicorn.run(
#       "app.main:app",
#       host="0.0.0.0",
#       port="8000",
#       log_level="info",
#       reload=True,
#       workers=1
#    )