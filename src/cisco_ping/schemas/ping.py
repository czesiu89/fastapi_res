from pydantic import BaseModel, AnyHttpUrl


class PingRequest(BaseModel):
    url: AnyHttpUrl
