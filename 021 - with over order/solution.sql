WITH PREPARED AS 
    (
        SELECT 
            LONG_W,
            ROW_NUMBER() OVER (ORDER BY LAT_N DESC) AS RN
        FROM 
            STATION
        WHERE 
            LAT_N < 137.2345
)
SELECT 
    CAST(LONG_W AS DECIMAL(18, 4))
FROM 
    PREPARED
WHERE 
    RN = 1
;