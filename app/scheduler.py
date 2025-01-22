# app/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from crawling.cu import crawl_cu
# from crawling.gs import crawl_gs25

scheduler = BackgroundScheduler()
scheduler.start()

def schedule_tasks():
    """스케줄 작업 등록"""
    scheduler.add_job(crawl_cu, CronTrigger(hour=0, minute=0))  # CU 크롤링 매일 자정 실행
    # scheduler.add_job(crawl_gs, CronTrigger(day=1, hour=0, minute=0))  # GS 크롤링 매달 1일 실행