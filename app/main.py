import uvicorn
import json
from datetime import datetime
from typing import Annotated, Any
from fastapi import FastAPI, Path
from ssl_checker import SSLChecker
from pydantic import BaseModel, JsonValue
from config import settings

app = FastAPI(
    root_path="/api/v{0}".format(settings.api_version),
    title=settings.api_name,
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    })
ssl_checker = SSLChecker()

class PingResponse(BaseModel):
    dang_ol: str
    server_timestamp: datetime
    status: str

class CheckResponse(BaseModel):
    api_version: str = "1.0"
    app: str = "ssl-checker-api"
    host: str = "example.com"
    status: str = "ok"
    result: JsonValue = {}

@app.get("/ping", summary="Health check")
def read_root() -> PingResponse:
    result = PingResponse(dang_ol="pong", server_timestamp=datetime.now(),status="ok")
    return result


@app.get("/check/{host:path}", summary="Checks SSL of a URL", response_model=CheckResponse)
async def check(host: Annotated[str, Path(title="The URL of the host")]) -> Any:
    """
    Check the hosts SSL certificate:

    - **host**: The URL of the host
    """
    args = ssl_checker.get_args({
        'hosts': [host]
        })
    result = json.loads(ssl_checker.show_result(args))
    response = {
        "api-version": settings.api_version,
        "app": "ssl-checker-api",
        "host": host,
        "status": "ok",
        "result": result[host]
    }
    return response

if __name__ == "__main__":
    uvicorn.run(app, host=settings.api_host, port=settings.api_port)