from fastapi import FastAPI, Response
from prometheus_client import Counter, Histogram, generate_latest
import random
import time

app = FastAPI(title="CivicCloud API")

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency",
    ["endpoint"]
)

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/ready")
def ready():
    return {"status": "ready"}

@app.get("/")
def home():
    start = time.time()
    REQUEST_COUNT.labels("GET", "/", "200").inc()
    REQUEST_LATENCY.labels("/").observe(time.time() - start)
    return {"service": "civiccloud-api", "status": "running"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    start = time.time()
    time.sleep(random.uniform(0.05, 0.2))
    REQUEST_COUNT.labels("GET", "/users/{user_id}", "200").inc()
    REQUEST_LATENCY.labels("/users/{user_id}").observe(time.time() - start)
    return {"user_id": user_id, "status": "active"}

@app.get("/fault/error")
def fault_error():
    start = time.time()
    REQUEST_COUNT.labels("GET", "/fault/error", "500").inc()
    REQUEST_LATENCY.labels("/fault/error").observe(time.time() - start)
    return Response(content="simulated error", status_code=500)

@app.get("/fault/latency")
def fault_latency():
    start = time.time()
    time.sleep(1.5)
    REQUEST_COUNT.labels("GET", "/fault/latency", "200").inc()
    REQUEST_LATENCY.labels("/fault/latency").observe(time.time() - start)
    return {"message": "simulated latency"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
