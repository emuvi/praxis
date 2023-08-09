WITH 
    PREPARED AS
        (
            SELECT
                LAT_N,
                ROW_NUMBER() OVER (ORDER BY LAT_N) AS RN
            FROM
                STATION
        ),
    COUNTED AS
        (
            SELECT 
                COUNT(*) AS CT
            FROM 
                STATION
        )

SELECT
    ROUND(
        AVG(PREPARED.LAT_N)
    , 4)
FROM
    PREPARED, COUNTED
WHERE
    PREPARED.RN BETWEEN COUNTED.CT / 2 AND COUNTED.CT / 2 + 1
;