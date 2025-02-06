from fastapi import APIRouter,Response
from ..database import client
from ..langchain import path

router = APIRouter(
    prefix="/device"
)


@router.get("/list")
async def getDevices():
    path.getPath()
    devicesList=[]
    dbs = await client.list_database_names()
    print(dbs)
    devices_db = client.get_database('devices')
    names= await devices_db.list_collection_names()
    print(names)
    device_collection = devices_db.get_collection("devicecollections")
    devices =device_collection.find().limit(5)
    async for dev in devices:
        dev["_id"] = str(dev["_id"])
        devicesList.append(dev)
    return devicesList