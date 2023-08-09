SELECT 
    C.company_code, C.founder, 
    COUNT(DISTINCT LM.lead_manager_code), 
    COUNT(DISTINCT SM.senior_manager_code), 
    COUNT(DISTINCT MN.manager_code), 
    COUNT(DISTINCT EM.employee_code) 
FROM 
    Company C 
    JOIN Lead_Manager LM USING (company_code) 
    JOIN Senior_Manager SM USING (company_code) 
    JOIN Manager MN USING (company_code) 
    JOIN Employee EM USING (company_code)
GROUP BY
    C.company_code, C.founder 
ORDER BY
    C.company_code