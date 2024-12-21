from fastapi import APIRouter, HTTPException
from models import WhitelistCreate, WhitelistBase
from mongo_file import mongo_insert_one


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