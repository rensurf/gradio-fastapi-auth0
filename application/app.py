import os
import sys
from urllib.parse import quote_plus, urlencode

import gradio as gr
from authlib.integrations.starlette_client import OAuth, OAuthError
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.sessions import SessionMiddleware

from interfaces.login import LoginInterface
from interfaces.logout import LogoutInterface
from interfaces.main_app import MainApplicationInterface

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if "/demo" in request.url.path:
            try:
                user = request.session.get("user")
                if not user:
                    return RedirectResponse(url="/login-page", status_code=302)
                print("User found in session, proceeding to demo")
            except Exception:
                return RedirectResponse(url="/login-page", status_code=302)
        return await call_next(request)


app = FastAPI()
load_dotenv()
app.add_middleware(AuthMiddleware)
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY"))

oauth = OAuth()
oauth.register(
    "auth0",
    client_id=os.getenv("AUTH0_CLIENT_ID"),
    client_secret=os.getenv("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{os.getenv("AUTH0_DOMAIN")}/.well-known/openid-configuration',
)


def get_user(request: Request):
    user = request.session.get("user")
    if user:
        return user["name"]
    return None


@app.get("/")
def public(request: Request):
    user = get_user(request)
    if user:
        return RedirectResponse(url="/demo")
    else:
        return RedirectResponse(url="/login-page")


@app.route("/login")
async def login(request: Request):
    if request.session.get("user"):
        return RedirectResponse(url="/demo")
    redirect_uri = request.url_for("auth")
    return await oauth.auth0.authorize_redirect(request, redirect_uri)


@app.route("/logout")
async def logout(request: Request):
    request.session.pop("user", None)
    return RedirectResponse(
        url="https://"
        + os.getenv("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": request.url_for("public"),
                "client_id": os.getenv("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )


@app.route("/auth")
async def auth(request: Request):
    try:
        access_token = await oauth.auth0.authorize_access_token(request)
        userinfo = dict(access_token)["userinfo"]
        request.session["user"] = userinfo
        return RedirectResponse(url="/demo", status_code=302)
    except OAuthError:
        return RedirectResponse(url="/")
    except Exception:
        return RedirectResponse(url="/")


login_demo = LoginInterface().interface
logout_demo = LogoutInterface().interface
main_app = MainApplicationInterface().interface

gr.mount_gradio_app(app, login_demo, path="/login-page")
gr.mount_gradio_app(app, logout_demo, path="/logout-page")
gr.mount_gradio_app(app, main_app, path="/demo")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)
