-- 코드를 입력하세요
SELECT
    BOOK_ID,
    AUTHOR_NAME,
    DATE_FORMAT(published_date, '%Y-%m-%d') AS PUBLISHED_DATE
FROM
    BOOK b
JOIN 
    AUTHOR a
    ON b.author_id = a.author_id 
WHERE
    category = '경제'
ORDER BY
    PUBLISHED_DATE
;