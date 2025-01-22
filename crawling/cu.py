from playwright.async_api import async_playwright
from app.database import save_to_db

async def crawl_cu():
    """CU 크롤링 로직"""
    product_list = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://cu.bgfretail.com/event/plus.do?category=event&depth2=1&sf=N")

        # "더보기" 버튼 반복 클릭
        while True:
            try:
                more_button = page.locator("a:has-text('더보기')")
                await more_button.wait_for(timeout=4000)
                if await more_button.is_visible():
                    await more_button.click()
                    await page.wait_for_timeout(200)
                else:
                    break
            except Exception as e:
                print("더보기 버튼이 더 이상 없습니다. 이유:", e)
                break

        # 상품 데이터 크롤링
        li_elements = page.locator("div.prodListWrap ul li")
        for i in range(await li_elements.count()):
            li = li_elements.nth(i)
            product_data = {
                "name": await li.locator("div.prod_wrap div.prod_text div.name p").text_content(),
                "price": await li.locator("div.prod_wrap div.prod_text div.price strong").text_content(),
                "event": await li.locator("div.badge span").get_attribute("class"),
                "image": await li.locator("div.prod_wrap div.prod_img img").get_attribute("src"),
                "tag": await li.locator("div.tag span").get_attribute("class"),
            }
            product_list.append(product_data)

        await browser.close()

    # MariaDB 저장
    save_to_db(product_list, store_name="CU")
