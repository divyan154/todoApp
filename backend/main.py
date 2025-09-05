import uvicorn


# Only run if this file is executed directly Like python main.py
if __name__ == "__main__": 
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)
