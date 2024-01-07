import json
import fastapi as fastapi
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.responses import FileResponse
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles
from .routers import user, book, review

app = fastapi.FastAPI()
app.include_router(user.router)
app.include_router(book.router)
app.include_router(review.router)


@app.get("/api")
async def root() -> str:
    return "server is UP!"

def use_route_names_as_operation_ids(application: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in application.routes:
        if isinstance(route, APIRoute):
            route: APIRoute = route
            route.operation_id = route.name

use_route_names_as_operation_ids(app)

openapi_schema = get_openapi(
    title="Testing!",
    version="0.1.0",
    routes=app.routes
)

with open('openapi.json', 'w') as f:
    json.dump(openapi_schema, f)


app.mount("/assets", StaticFiles(directory="../frontend/dist/assets"), name="static")

# Simply the root will return our Svelte build
@app.get("/{cool:path}", response_class=FileResponse)
async def main(cool: str):
    return "../frontend/dist/index.html"
