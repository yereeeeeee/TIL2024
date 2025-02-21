
WITH AVAILABLE_CAR AS (
    SELECT
        car.CAR_ID,
        car.CAR_TYPE,
        car.DAILY_FEE,
        CASE
            WHEN MAX(
                CASE
                    WHEN '2022-11-01' BETWEEN START_DATE AND END_DATE THEN 1
                    WHEN '2022-11-30' BETWEEN START_DATE AND END_DATE THEN 1
                    ELSE 0
                END
            ) = 0 THEN '대여 가능'
            ELSE '불가능'
        END AS AVAILABILITY
    FROM
        CAR_RENTAL_COMPANY_CAR car
    JOIN
        CAR_RENTAL_COMPANY_RENTAL_HISTORY history
        ON car.CAR_ID = history.CAR_ID
    GROUP BY
        car.CAR_ID, car.CAR_TYPE, car.DAILY_FEE
),
DISCOUNTED_FEE AS (
    SELECT
        car.CAR_ID,
        car.CAR_TYPE,
        (car.DAILY_FEE * 30) AS ORIGINAL_FEE,
        CASE
            WHEN plan.DURATION_TYPE = '30일 이상' THEN (car.DAILY_FEE * 30) * (1 - plan.DISCOUNT_RATE / 100)
            ELSE (car.DAILY_FEE * 30)
        END AS FEE
    FROM
        AVAILABLE_CAR car
    JOIN
        CAR_RENTAL_COMPANY_DISCOUNT_PLAN plan
    ON
        car.CAR_TYPE = plan.CAR_TYPE
    WHERE
        car.AVAILABILITY = '대여 가능' 
        AND plan.DURATION_TYPE = '30일 이상'
)
SELECT
    CAR_ID,
    CAR_TYPE,
    ROUND(FEE, 0) AS FEE
FROM
    DISCOUNTED_FEE
WHERE
    FEE BETWEEN 500000 AND 2000000
ORDER BY
    FEE DESC,
    CAR_TYPE ASC,
    CAR_ID DESC;
