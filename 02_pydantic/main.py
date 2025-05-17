from typing import Annotated, Literal
from annotated_types import Gt
from pydantic import BaseModel


class UserData(BaseModel):
    name: str  
    color: Literal['Black' , 'red']  
    weight: Annotated[float, Gt(0)]  
    item: dict[str, list[tuple[int, bool, float]]]  


print(
    UserData(
        name="Arishba Khan",
        color='Black',
        weight=1.8,
        item={'Football': [(1, True, 0.1)]},
    )
)
print(
    UserData(
        name=7, #this line throws an error 
        color='red',
        weight=2.8,
        item={'basketball': [(1, True, 0.1)]},
    )
)