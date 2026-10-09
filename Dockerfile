FROM python:3.12-slim
WORKDIR /app
COPY bench.py /app/bench.py
COPY tests /app/tests
CMD ["python", "-m", "unittest", "discover", "-s", "tests", "-v"]
