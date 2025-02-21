WITH HEAVY_SELLER AS (
    SELECT 
        WRITER_ID,
        SUM(
            CASE
                WHEN STATUS = 'DONE' THEN PRICE
                ELSE 0 
            END
        ) AS TOTAL_SALES
    FROM
        USED_GOODS_BOARD
    GROUP BY
        WRITER_ID
)

SELECT
    u.USER_ID,
    u.NICKNAME,
    h.TOTAL_SALES
FROM
    USED_GOODS_USER u
JOIN
    HEAVY_SELLER h
    ON u.USER_ID = h.WRITER_ID
WHERE
    h.TOTAL_SALES >= 700000
ORDER BY
    h.TOTAL_SALES
;