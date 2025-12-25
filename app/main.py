from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import sys
import os
app = FastAPI(title="DevOps Portfolio API")

@app.get("/", response_class=HTMLResponse)
def read_root():

    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(base_dir, "templates", "index.html")
    
    try:
        with open(template_path, "r", encoding="utf-8") as f:
            content = f.read()
        return HTMLResponse(content=content, status_code=200)
    except FileNotFoundError:
        return HTMLResponse(
            content="<html><body><h1>Template Not Found</h1><p>請確認 templates/index.html 檔案存在。</p></body></html>", 
            status_code=404
        )

@app.get("/version")
def get_version():
    return {
        "version": "1.0.1",
        "python_version": sys.version,
        "environment": "production",
        "owner": "Your Name"
    }

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Service is healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)