from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import sys
import os
app = FastAPI(title="DevOps API")

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
            content="<html><body><h1>Template Not Found</h1><p>確認 templates/index.html</p></body></html>", 
            status_code=404
        )

@app.get("/version")
def get_version():
    return {
        "version": "1.1.0",
        "python_version": sys.version,
        "owner": "ec2-user"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)