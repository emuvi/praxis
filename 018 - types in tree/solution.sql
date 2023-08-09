SELECT BT.N,
    CASE
        WHEN P IS NULL THEN 'Root'
        WHEN C > 0 THEN 'Inner'
        ELSE 'Leaf'
    END AS T
FROM
    (
        SELECT
            B1.N, B1.P, 
            (
                SELECT 
                    COUNT(*)
                FROM
                    BST B2
                WHERE
                    B2.P = B1.N       
            ) AS C
            FROM
                BST B1
    ) BT
ORDER BY
    BT.N
;