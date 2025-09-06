from fastapi import FastAPI

app = FastAPI(
    title="My FastAPI Service",
    version="1.0.0",
    description="Example FastAPI service running on Python 3.10 with Swagger UI.",
    docs_url="/docs",       # Swagger UI
    redoc_url="/redoc"      # ReDoc (optional)
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def read_root():
    return {"hello": "world"}
