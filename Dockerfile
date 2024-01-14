FROM ubuntu:22.04

COPY --from=node:18.16.0-slim / /

WORKDIR /usr/local/web-dev-library

RUN apt-get update && apt-get install -y \
  python3 \
  python3-pip

COPY . .

RUN cd frontend && npm i && npm run build && cd ..

RUN cd backend && python3 -m pip install -r requirements.txt --break-system-packages

WORKDIR /usr/local/web-dev-library/backend

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
