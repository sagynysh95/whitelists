from pydantic import BaseModel, Field, model_validator
from typing import Optional
from datetime import datetime, timedelta
from enum import Enum
from fastapi import HTTPException
from dateutil.relativedelta import relativedelta


class WeekdayEnum(str, Enum):
    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"
    sunday = "Sunday"


class MonthEnum(str, Enum):
    january = "January"
    february = "February"
    march = "March"
    april = "April"
    may = "May"
    June = "June"
    july = "July"
    august = "August"
    september = "September"
    october = "October"
    november = "November"
    december = "December"


class WhitelistBase(BaseModel):
    user_id: Optional[str] = Field(
        default=None
    )
    start_time: Optional[str] = Field(
        default=None,
        description="start time for permission"
    )
    end_time: Optional[str] = Field(
        default=None, 
        description="permission expiration time"
    )
    minutes: Optional[int] = Field(
        default=None,
        description="minutes for permission, end_time calculates automatically"
    )
    hours: Optional[int] = Field(
        default=None,
        description="hours for permission, end_time calculates automatically"
    )
    days: Optional[int] = Field(
        default=None,
        description="days for permission, end_time calculates automatically"
    )
    weeks: Optional[int] = Field(
        default=None,
        description="weeks for adding to calculate permission end_time"
    )
    months: Optional[int] = Field(
        default=None,
        description="months for adding to calculate permission end_time"
    ) 
    years: Optional[int] = Field(
        default=None,
        description="years for adding to calculate permission end_time"
    ) 
    weekday: Optional[WeekdayEnum] = Field(
        default=None,
        description="exact weekday for permission"
    )
    month: Optional[MonthEnum] = Field(
        default=None,
        description="exact month for permission"
    )
    hours_start: Optional[int] = Field(
        default=None
    )


class WhitelistCreate(WhitelistBase):
    user_id: str
    

    @model_validator(mode="before")
    def validate_times(cls, values):
        start_time = values.get("start_time")
        if values.get("end_time") and any([values.get("hours"), values.get("minutes"), values.get("days"), values.get("weeks"), values.get("months"), values.get("years")]):
            raise HTTPException(status_code=422, detail="end_time is defined, no need for days, months, etc")
        
        if start_time is None:
            values["start_time"] = datetime.now().replace(microsecond=0)
            start_time = values["start_time"]
        else:
            try:
                if len(start_time) == 10:
                    start_time += " 00:00:00"
                start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                raise HTTPException(status_code=422, detail="start_time format must be 'YYYY-MM-DD HH:MM:SS'")
        values["start_time"] = str(start_time)
        end_time = start_time

        if values.get("minutes"):
            end_time += timedelta(minutes=values["minutes"])
        if values.get("hours"):
            end_time += timedelta(hours=values["hours"])
        if values.get("days"):
            end_time += timedelta(days=values["days"])
        if values.get("weeks"):
            end_time += timedelta(weeks=values["weeks"])
        if values.get("months"):
            end_time += relativedelta(months=+values["months"])
        if values.get("years"):
            values["end_time"] = str(end_time.replace(year=end_time.year + values["years"]))
        else:
            values["end_time"] = str(end_time)
        return values

        

    


