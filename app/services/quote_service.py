import aiohttp
from app.db.pool import pool
from app.models.quote import Quote, QuoteBookmark
from app.models.question import ReflectionQuestion

# 웹에서 명언 스크래핑 후 DB 저장
async def fetch_and_store_quotes():
    url = "https://quotes.toscrape.com/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            html = await resp.text()
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    async with pool.acquire() as conn:
        for div in soup.select(".quote"):
            text = div.select_one(".text").get_text(strip=True)
            author = div.select_one(".author").get_text(strip=True)
            exists = await conn.fetchval("SELECT 1 FROM quotes WHERE text=$1 AND author=$2", text, author)
            if not exists:
                await conn.execute(
                    "INSERT INTO quotes(text, author, source_url) VALUES($1, $2, $3)",
                    text, author, url
                )

# 랜덤 명언 조회
async def get_random_quote():
    async with pool.acquire() as conn:
        row = await conn.fetchrow("SELECT id, text, author FROM quotes ORDER BY RANDOM() LIMIT 1")
        return Quote(**row)

# 북마크 추가
async def add_bookmark(user_id: int, quote_id: int):
    async with pool.acquire() as conn:
        exists = await conn.fetchval("SELECT 1 FROM quote_bookmarks WHERE user_id=$1 AND quote_id=$2", user_id, quote_id)
        if exists:
            return False
        await conn.execute("INSERT INTO quote_bookmarks(user_id, quote_id) VALUES($1,$2)", user_id, quote_id)
        return True

# 북마크 조회
async def get_bookmarks(user_id: int):
    async with pool.acquire() as conn:
        rows = await conn.fetch(
            "SELECT q.id, q.text, q.author FROM quotes q "
            "JOIN quote_bookmarks qb ON q.id = qb.quote_id "
            "WHERE qb.user_id=$1", user_id
        )
        return [Quote(**r) for r in rows]

# 랜덤 질문
async def get_random_question():
    async with pool.acquire() as conn:
        row = await conn.fetchrow("SELECT id, text FROM reflection_questions ORDER BY RANDOM() LIMIT 1")
        return ReflectionQuestion(**row)
