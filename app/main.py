from fastapi import FastAPI
import sys

# 初始化 FastAPI 應用
app = FastAPI(title="Cloud-Native Monitoring Hub")

@app.get("/")
def read_root():
    return {
        "message": "Hello from FastAPI on AWS EC2",
        "status": "running",
        "system": "Cloud-Native Project"
    }

@app.get("/version")
def get_version():
    return {
        "version": "1.0.1",
        "python_version": sys.version,
        "environment": "production"
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    # 本地測試時可以使用: python app/main.py
    uvicorn.run(app, host="0.0.0.0", port=8000)