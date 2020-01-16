import uvicorn

from app.main import app

uvicorn.run(app, host="0.0.0.0", port=8000, log_level="trace")

# cd src
# uvicorn app.main:app --reload --host 0.0.0.0 --log-level trace