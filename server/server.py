from fastapi import FastAPI
from pydantic import BaseModel
import socket
import time
import uuid

app = FastAPI(
    title="SMO Distributed Data Processing Server",
    version="1.0"
)


class DataRequest(BaseModel):
    client_id: str
    numbers: list[float]


@app.get("/")
def root():
    return {
        "service": "SMO Distributed Data Processing Server",
        "status": "running",
        "hostname": socket.gethostname()
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "hostname": socket.gethostname()
    }


@app.post("/process")
def process_data(request: DataRequest):

    start_time = time.perf_counter()

    numbers = request.numbers

    if not numbers:
        return {
            "error": "numbers list cannot be empty"
        }

    total = sum(numbers)

    result = {
        "request_id": str(uuid.uuid4()),
        "client_id": request.client_id,
        "server_hostname": socket.gethostname(),
        "count": len(numbers),
        "sum": total,
        "average": total / len(numbers),
        "minimum": min(numbers),
        "maximum": max(numbers)
    }

    processing_time = time.perf_counter() - start_time

    result["processing_time_ms"] = round(
        processing_time * 1000,
        3
    )

    return result