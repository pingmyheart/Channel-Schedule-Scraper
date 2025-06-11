from pydantic import BaseModel


class ServiceResponse(BaseModel):
    response_code: int
    response_message: str
