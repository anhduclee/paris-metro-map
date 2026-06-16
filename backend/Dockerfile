FROM python:3.12-slim as builder
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim as runner
WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
EXPOSE 8000
COPY . .
CMD ["uvicorn","--host","0.0.0.0","--port","8000","app.main:app"]