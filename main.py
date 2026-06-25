from fastapi import FastAPI


from controller.controller import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():
    return {"msg": "API working correctly."}