# app/routers/crawling.py
from fastapi import APIRouter
from crawling.cu import crawl_cu
# from crawling.gs25 import crawl_gs25

router = APIRouter()

@router.get("/run-crawling/cu")
async def run_crawling_cu():
    """CU 크롤링 실행"""
    result = await crawl_cu()
    return result

# @router.get("/run-crawling/gs25")
# async def run_crawling_gs():
#     """GS 크롤링 실행"""
#     await crawl_gs25()
#     return {"status": "GS25 crawling completed"}