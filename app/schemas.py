

from pydantic import BaseModel, ConfigDict


class ismaeilCreate(BaseModel):
    age: int
    gender : int
    pressurehight: int
    pressurelow : int
    glucose : int
    kcm:float
    troponin: float
    impulse: float
    
    model_config = ConfigDict(from_attributes=True)
class ismaeilResponse(ismaeilCreate):
    id: int
    status: int | None=None
    model_config = ConfigDict(from_attributes=True)

