# fastapi-crud

source: https://testdriven.io/blog/fastapi-crud/

## HOWTO run in VS Code:
```
# cd src
# uvicorn app.main:app --reload --host 0.0.0.0 --log-level trace
```

## HOWTO debug in VS Code:
DEBUG: (must run *.py, so create `src/manage.py`) 

launch.json 
```
        { 
            "name": "DEBUG manage.py", 
            "type": "python", 
            "request": "launch", 
            "program": "${workspaceFolder}/src/manage.py", 
            "console": "integratedTerminal", 
            "cwd": "${workspaceFolder}/src" 
        } 
```

manage.py 
```
import uvicorn 
# from app.main import app 
uvicorn.run("app.main:app", host="0.0.0.0", port=8000, log_level="trace") 
```