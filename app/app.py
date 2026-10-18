from flask import Flask, request, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import socket
import time

app = Flask(__name__)

REQUESTS = Counter(
    "flask_http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)
LATENCY = Histogram(
    "flask_http_request_duration_seconds",
    "HTTP request duration in seconds",
    ["method", "endpoint"]
)

@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def record_metrics(response):
    if request.path != "/metrics":
        endpoint = request.url_rule.rule if request.url_rule else "not_found"
        REQUESTS.labels(request.method, endpoint, str(response.status_code)).inc()
        LATENCY.labels(request.method, endpoint).observe(
            time.time() - getattr(request, "start_time", time.time())
        )
    return response

@app.route("/")
def home():
    return f"DevOps Project - Main + Feature Version! Hostname: {socket.gethostname()}"

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/version")
def version():
    return {"version": "1.1"}

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
