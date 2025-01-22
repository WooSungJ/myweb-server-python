import asyncio
import platform
from fastapi import FastAPI
from app.scheduler import schedule_tasks
from app.routers import crawling
from playwright._impl._installer import install_default_browsers

app = FastAPI()

# Playwright 설치
@app.on_event("startup")
async def setup_playwright():
    """서버 시작 시 Playwright 브라우저 설치"""
    print("Playwright 브라우저 설치 중...")
    await asyncio.to_thread(install_default_browsers)
    print("Chromium 설치 완료.")

# 스케줄 작업 등록
# @app.on_event("startup")
# def startup_event():
#     """애플리케이션 시작 시 스케줄 작업 등록"""
#     schedule_tasks()

# 라우터 등록
app.include_router(crawling.router)

@app.get("/")
async def root():
    return {"message": "Welcome"}

# FastAPI 실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
