**CREATE INDEX idx_diary_created_at ON diary_entries(created_at);**

**CREATE INDEX idx_diary_title_content ON diary_entries USING GIN (to_tsvector(‘english’, title || ‘ ‘ || content));**

**INSERT INTO diary_entries (user_id, title, content) VALUES (1, ‘오늘의 일기’, ‘내용입니다.’);**

**SELECT * FROM diary_entries WHERE id = 123;**

**UPDATE diary_entries SET title = ‘수정된 제목’, content = ‘수정된 내용’, updated_at = CURRENT_TIMESTAMP WHERE id = 123;**

**DELETE FROM diary_entries WHERE id = 123;**

**SELECT * FROM diary_entries WHERE title ILIKE ‘%keyword%’ OR content ILIKE ‘%keyword%’ ORDER BY created_at DESC LIMIT 10 OFFSET 0;**

**SELECT * FROM diary_entries ORDER BY created_at ASC LIMIT 10 OFFSET 0;**

**SELECT * FROM diary_entries ORDER BY created_at DESC LIMIT 10 OFFSET 20;** — Example: 3페이지 (10개씩)
