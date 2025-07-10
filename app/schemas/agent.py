from pydantic import BaseModel

class AgentBase(BaseModel):
    name: str
    warehouse_id: int

class AgentCreate(AgentBase):
    pass

class AgentOut(AgentBase):
    id: int
    checked_in: bool
    class Config:
        orm_mode = True