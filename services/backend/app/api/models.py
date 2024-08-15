from pydantic import BaseModel, Field, field_validator
from typing import List

class WorkExperience(BaseModel):
    position: str = Field(..., min_length=1, max_length=100)
    company: str = Field(..., min_length=1, max_length=100)
    date: str = Field(..., min_length=1, max_length=50)

class Education(BaseModel):
    school: str = Field(..., min_length=1, max_length=100)
    date: str = Field(..., min_length=1, max_length=50)

class CVData(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    career_objectives: str = Field(..., min_length=1, max_length=500)
    work_experience: List[WorkExperience] = Field(..., min_items=1)
    education: List[Education] = Field(..., min_items=1)

    @field_validator("name")
    def name_must_contain_space(cls, v):
        if " " not in v:
            raise ValueError("must contain at least first and last name")
        return v