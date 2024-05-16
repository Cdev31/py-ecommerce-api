from typing import Any, TypedDict, Optional
from enum import Enum


class StatusCode( Enum ):
    OK = 200
    CREATED = 201
    NOT_FOUND = 404
    UNAUTHORIZED = 400
    INTERNAL_ERROR = 500


class ResponseType( TypedDict ):
    status: StatusCode
    error: Optional[ str | None ]
    message: Optional[ str | None ]
    response: Any
