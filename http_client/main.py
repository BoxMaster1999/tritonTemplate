from fastapi import FastAPI, status

from src.routes import textgen_router

app = FastAPI(title='ClientTemplate',
              description='Fastapi client for triton-server',
              version='0.1')

# Adding v1 namespace route
app.include_router(textgen_router)


@app.get('/health',
         tags=['System probs'])
def health() -> int:
    return status.HTTP_200_OK
