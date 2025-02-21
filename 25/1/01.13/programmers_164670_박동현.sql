SELECT
    b.USER_ID,
    b.NICKNAME,
    
    CONCAT(
        b.CITY, ' ',
        b.STREET_ADDRESS1, ' ',
        b.STREET_ADDRESS2
    ) AS 전체주소,
    
    CONCAT(
        SUBSTR(b.TLNO, 1, 3), '-',
        SUBSTR(b.TLNO, 4, 4), '-',  
        SUBSTR(b.TLNO, 8)
    ) AS 전화번호
FROM
    USED_GOODS_BOARD a
JOIN
    USED_GOODS_USER b
ON 
    a.WRITER_ID = b.USER_ID
GROUP BY
        b.USER_ID, b.NICKNAME, b.CITY, 
        b.STREET_ADDRESS1, b.STREET_ADDRESS2, b.TLNO
HAVING
    COUNT(a.WRITER_ID) >= 3
ORDER BY 
    WRITER_ID DESC
;