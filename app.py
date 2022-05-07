from sanic import Sanic
from sanic import response
from sanic_ext import cors

app = Sanic("SignupManagement")
app.config.CORS_ORIGINS = "http://localhost:3000,https://*sveltechi.vercel.app,https://sveltechi.com"

@app.route("/",["GET"])
async def hello(request):
    return response.json({"hello":"world"})

#app.add_route(signup,"/",["GET"])