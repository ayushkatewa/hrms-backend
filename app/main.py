import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import employees, attendance, leave, dashboard, recruitment, performance, finance, payroll
from app.routers import assets

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="HRMS API", version="1.0.0")

# Global Exception Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error", "detail": str(exc)},
    )

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for dev/fix
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employees.router)
app.include_router(attendance.router)
app.include_router(leave.router)
app.include_router(dashboard.router)
app.include_router(recruitment.router)
app.include_router(performance.router)
app.include_router(finance.router)
app.include_router(payroll.router)
app.include_router(assets.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to HRMS API", "status": "active"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
