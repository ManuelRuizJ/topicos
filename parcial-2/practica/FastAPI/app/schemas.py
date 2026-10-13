from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict, field_validator

class CancionBase(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=200)
    artista: str = Field(..., min_length=1, max_length=200)
    genero: str | None = Field(default=None, max_length=100)
    anio: int | None = Field(default=None, ge=1900, le=datetime.now().year())

    @field_validator("titulo", "artista")
    @classmethod
    def no_vacios(cls, v = str) -> str:
        if not v.strip():
            raise ValueError("No puede estar vacio")
        return v.strip()


class CancionCreate(CancionBase):
    pass


class CancionUpdate(BaseModel):
    titulo: str | None =  Field(default=None, max_length=200)