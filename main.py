import fastapi

# uvicorn main:api --reload
# lsof -i :8000
# kill -9 <process_id>
api = fastapi.FastAPI()


@api.get('/hello')
def api_hello():
    return {"hello": 'from api!'}
