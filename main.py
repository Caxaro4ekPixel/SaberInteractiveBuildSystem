from fastapi import FastAPI, Request
from utils import get_sorted_tasks_by_build

app = FastAPI()


@app.post("/get_tasks/")
async def get_tasks(request: Request):
    """
        Get sorted tasks by build
        .. example::
           $ curl http://<address>/get_tasks -X POST
             -d '{
                    "build": "<build name>",
                }'
    """
    request_body = await request.json()
    if not request_body:
        return {"error": "No fields"}
    if "build" not in request_body:
        return {"error": "No build field"}
    res, tasks_temp_by_build, status = get_sorted_tasks_by_build(request_body["build"])

    if status:
        return {"sorted": res, "not sorted": tasks_temp_by_build}
    else:
        return {"error": "Error in getting tasks"}
