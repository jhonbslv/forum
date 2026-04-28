fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from model import consulta_alunos, add_aluno

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):    
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"context":consulta_alunos()})

@app.post("/add")
async def adicionar(request: Request):
    form = await request.form()

    add_aluno(form.get("nome")) 

    return RedirectResponse(url="/", status_code=303)