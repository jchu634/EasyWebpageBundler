import uvicorn
"""Initialize Flask app."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse, ORJSONResponse
from config import Settings
import os

def create_app(aargs=None):
    if Settings.ENV == "development":
        app = FastAPI()
    else:
        app = FastAPI(docs_url=None, redoc_url=None)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app

app = create_app()

@app.get("/")
@app.get("/{path:path}", responses={200: {"description": "Success"}, 404: {"description": "Not Found"}})
def path(path:str=None):
    print(path)
    if path.endswith((".js", ".txt", ".css",".html", ".woff2")):
        return FileResponse(os.path.join(Settings.STATIC_FOLDER,path))
    elif path and path[-1] == "/":
        return HTMLResponse(open(os.path.join(Settings.STATIC_FOLDER,path)+"index.html","r").read())    
    elif not path:
        return HTMLResponse(open(os.path.join(Settings.STATIC_FOLDER,"index.html"),"r").read())
    elif Settings.ERR404 == "true":
        return HTMLResponse(open(os.path.join(Settings.STATIC_FOLDER,"404.html"),"r").read())
    return ORJSONResponse(content={"error": "File not found"}, status_code=404)


if __name__ == "__main__":
    uvicorn.run("fastapiserver:app", port=6789, host="0.0.0.0", reload=True)