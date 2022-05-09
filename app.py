import os

from sanic import Sanic
from sanic import response, handlers
from dotenv import load_dotenv

from blueprints import signup

load_dotenv()
app = Sanic("EventManagement")

app.config.GOOGLE_AUTH = os.getenv('GOOGLE_AUTH', False)
app.config.CORS_ORIGINS = "http://localhost:3000,https://*sveltechi.vercel.app,https://sveltechi.com"
app.config.FALLBACK_ERROR_FORMAT = 'json'

async def hello(request):
    return response.json({"running": True})

app.add_route(hello,"/",["GET"])
app.blueprint(signup.bp)

