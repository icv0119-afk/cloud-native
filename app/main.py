from fastapi import FastAPI
import sys

# 初始化 FastAPI 應用
app = FastAPI(title="Cloud-Native Monitoring Hub")

@app.get("/")
def read_root():
    """
    基礎進入點，驗證服務是否正常運行
    """
    return {
        "message": "Hello from FastAPI on AWS EC2",
        "status": "running",
        "system": "Cloud-Native Project"
    }

@app.get("/version")
def get_version():
    """
    版本管理路由，用於部署後的版本驗證
    """
    return {
        "version": "1.0.1",
        "python_version": sys.version,
        "environment": "production"
    }

@app.get("/health")
def health_check():
    """
    健康檢查路由，供 Nginx 或 Docker Healthcheck 使用
    """
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    # 本地測試時可以使用: python app/main.py
    uvicorn.run(app, host="0.0.0.0", port=8000)