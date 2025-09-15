from fastapi import FastAPI
from app.routes import document_routes

app = FastAPI(
    title="Mortgage Document API",
    version="1.0.0",
    description="API for validating mortgage documents"
)

# Register routes
app.include_router(document_routes.router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Mortgage Document API is running 🚀"}
