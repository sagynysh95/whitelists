from fastapi import APIRouter, HTTPException
from models import WhitelistCreate, WhitelistBase
from mongo_file import mongo_insert_one, mongo_find_all, mongo_find_by_user_id
from typing import List, Optional, Union
from datetime import datetime


router = APIRouter(prefix="/whitelist", tags=["whitelist"])


@router.post("/", status_code=201, response_model=WhitelistBase)
def create_permission_by_userid(data: WhitelistCreate):
    try:
        data_dict = data.model_dump(exclude_unset=False)
        result = mongo_insert_one(data_dict["user_id"], data_dict)
        print(result)
        return WhitelistBase.model_validate(result)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Error: {e}")
    

@router.get("/", status_code=200, response_model=Union[List[WhitelistBase], dict])
def check_permission(
    user_id: Optional[str] = None,
    date: Optional[str] = None
):
    try:
        if not user_id and not date: 
            result = mongo_find_all()
            return [WhitelistBase.model_validate(data) for data in result]
        
        if len(date) == 10:
            date += " 00:00:00"

        check_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        record = mongo_find_by_user_id(user_id)
        if not record:
            return {"result": False, "message": "User ID not found"}
        
        start_time = datetime.strptime(record["start_time"], "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(record["end_time"], "%Y-%m-%d %H:%M:%S")

        if not (start_time <= check_date <= end_time):
            return {"result": False, "message": "Date not in range"}
        
        if record.get("weekday"):
            weekday = check_date.strftime("%A")
            if weekday != record["weekday"]:
                return {"result": False, "message": "Weekday does not match"}
            
        if record.get("month"):
            month = check_date.strftime("%B")
            if month != record["month"]:
                return {"result": False, "message": "Month does not match"}
            
        return {"result": True}

    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Error: {e}")