-- 코드를 입력하세요
SELECT
    CONCAT(
        '/home/grep/src/',
        b.BOARD_ID, '/',
        b.FILE_ID,
        b.FILE_NAME,
        b.FILE_EXT
    ) AS FILE_PATH
FROM
USED_GOODS_BOARD a
JOIN USED_GOODS_FILE b
ON a.BOARD_ID = b.BOARD_ID
WHERE a.VIEWS = (
    SELECT 
        MAX(VIEWS)
    FROM
        USED_GOODS_BOARD
    )
ORDER BY b.FILE_ID DESC;