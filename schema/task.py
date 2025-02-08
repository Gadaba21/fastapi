from pydantic import BaseModel, model_validator


class Task(BaseModel):
    id: int
    name: str | None = None
    pomodoro_count: int | None = None
    category_id: int

    @model_validator(mode='after')
    @classmethod
    def check_name(self):
        if self.name is None and self.pomodoro_count is None:
            raise ValueError('Error')
        return self
