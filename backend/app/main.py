from datetime import datetime
from pathlib import Path
from fastapi import FastAPI, Form, Request, HTTPException

from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .db import (
    init_db,
    list_posts,
    get_post,
    search_posts_by_title,
    create_post,
    delete_post,
    get_prev_post_id,
    get_next_post_id,
)


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="IT Club PM Demo (Jinja2 + HTMX + SQLite)")

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def index(request: Request, q: str | None = None):
    q_clean = (q or "").strip()

    if q_clean:
        posts = search_posts_by_title(q_clean)
    else:
        posts = list_posts()

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "posts": posts, "q": q_clean},
    )

@app.get("/new", response_class=HTMLResponse)
def new_post_form(request: Request):
    return templates.TemplateResponse("new.html", {"request": request})


@app.post("/posts", response_class=HTMLResponse)
def create_post_action(
    request: Request,
    title: str = Form(""),
    content: str = Form(""),
):
    title = title.strip()
    content = content.strip()

    # 검증(Validation)
    if not title:
        return templates.TemplateResponse(
            "new.html",
            {"request": request, "error": "제목을 입력해주세요.", "title": title, "content": content},
            status_code=400,
        )

    if len(title) > 50:
        return templates.TemplateResponse(
            "new.html",
            {"request": request, "error": "제목은 50자 이하여야 합니다.", "title": title, "content": content},
            status_code=400,
        )

    if not content:
        return templates.TemplateResponse(
            "new.html",
            {"request": request, "error": "내용을 입력해주세요.", "title": title, "content": content},
            status_code=400,
        )

    created_at = datetime.now().isoformat(timespec="seconds")
    post_id = create_post(title=title, content=content, created_at=created_at)

    # 작성 후 상세 페이지로 이동
    return RedirectResponse(url=f"/posts/{post_id}", status_code=303)



@app.get("/posts/{post_id}", response_class=HTMLResponse)
def detail(request: Request, post_id: int):
    post = get_post(post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="post not found")

    prev_id = get_prev_post_id(post_id)
    next_id = get_next_post_id(post_id)

    return templates.TemplateResponse(
        "detail.html",
        {"request": request, "post": post, "prev_id": prev_id, "next_id": next_id},
    )


@app.delete("/posts/{post_id}", response_class=HTMLResponse)
def delete_post_action(request: Request, post_id: int):
    delete_post(post_id)
    posts = list_posts()
    return templates.TemplateResponse(
        "_posts.html",
        {"request": request, "posts": posts},
    )
@app.get("/api/posts")
def api_list_posts(q: str | None = None):
    q_clean = (q or "").strip()

    if q_clean:
        posts = search_posts_by_title(q_clean)
    else:
        posts = list_posts()

    # sqlite3.Row는 그대로 JSON이 안 될 수 있어서 dict로 변환
    return {
        "count": len(posts),
        "query": q_clean,
        "posts": [
            {
                "id": p["id"],
                "title": p["title"],
                "content": p["content"],
                "created_at": p["created_at"],
            }
            for p in posts
        ],
    }
@app.get("/api/posts")
def api_list_posts(q: str | None = None):
    q_clean = (q or "").strip()

    if q_clean:
        rows = search_posts_by_title(q_clean)
    else:
        rows = list_posts()

    # sqlite3.Row -> dict로 변환 (JSON으로 내보내기 위해)
    posts = [
        {
            "id": r["id"],
            "title": r["title"],
            "content": r["content"],
            "created_at": r["created_at"],
        }
        for r in rows
    ]

    return {
        "count": len(posts),
        "query": q_clean,
        "posts": posts,
    }
