from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from .routers.iris_router import iris_router

app = FastAPI()

# Redireccionamiento a la página de iris
@app.get("/", response_class=RedirectResponse)
async def root():
    return RedirectResponse("/api/iris")

# ==========================
#       IRIS REST API
# ==========================
app.include_router(iris_router, prefix="/api/iris")
# ==========================
#    END IRIS REST API
# ==========================    
