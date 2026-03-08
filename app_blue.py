from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"version": "BLUE", "message": "Production API running"}
