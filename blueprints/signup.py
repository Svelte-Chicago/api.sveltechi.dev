from datetime import datetime


from sanic import exceptions
from sanic import response
from sanic import Blueprint

from eventreg import event

bp = Blueprint("signup", url_prefix="signup")

async def event_middleware(request):
    if not request.app.config.GOOGLE_AUTH:
        raise exceptions.ServerError('unable to make data connection')

async def signup_create(request) -> response:
    return response.json({"signup": "true"})

async def signup_confirm(request) -> response:
    return response.json({"signup": "confirmed"})

async def signup_update(request) -> response:
    return response.json({"signup": "updated"})

async def signup_delete(request) -> response:
    return response.json({"signup": "deleted"})

bp.add_route(signup_create, "/")
bp.add_route(signup_confirm, "/confirm")
bp.add_route(signup_update, "/update")
bp.add_route(signup_delete, "/delete")
bp.middleware(event_middleware)
