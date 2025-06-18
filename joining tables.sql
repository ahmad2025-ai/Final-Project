SELECT * FROM std_pr_math;
SELECT * FROM std_pr_math
WHERE sex='M';

SELECT * FROM std_pr_math
WHERE sex='F';

##joining both tables
SELECT
    *
FROM
    std_pr_math AS m
JOIN
    student_per_port AS p
ON
    m.school = p.school AND
    m.sex = p.sex AND
    m.age = p.age AND
    m.address = p.address AND
    m.famsize = p.famsize AND
    m.Pstatus = p.Pstatus AND
    m.Medu = p.Medu AND
    m.Fedu = p.Fedu AND
    m.Mjob = p.Mjob AND
    m.Fjob = p.Fjob AND
    m.reason = p.reason AND
    m.guardian = p.guardian;

CREATE TABLE joined_student AS
SELECT
    m.school AS m_school,
    m.sex AS m_sex,
    m.age AS m_age,
    m.address AS m_address,
    m.famsize AS m_famsize,
    m.Pstatus AS m_Pstatus,
    m.Medu AS m_Medu,
    m.Fedu AS m_Fedu,
    m.Mjob AS m_Mjob,
    m.Fjob AS m_Fjob,
    m.reason AS m_reason,
    m.guardian AS m_guardian,
    -- Add more m.* fields as needed
    p.school AS p_school,
    p.sex AS p_sex,
    p.age AS p_age,
    p.address AS p_address,
    p.famsize AS p_famsize,
    p.Pstatus AS p_Pstatus,
    p.Medu AS p_MEdu,
    p.Fedu AS p_FEdu,
    p.Mjob AS p_Mjob,
    p.Fjob AS p_Fjob,
    p.reason AS p_reason,
    p.guardian AS p_guardian
    -- Add more p.* fields as needed
FROM
    std_pr_math AS m
JOIN
    student_per_port AS p
ON
    m.school = p.school AND
    m.sex = p.sex AND
    m.age = p.age AND
    m.address = p.address AND
    m.famsize = p.famsize AND
    m.Pstatus = p.Pstatus AND
    m.Medu = p.Medu AND
    m.Fedu = p.Fedu AND
    m.Mjob = p.Mjob AND
    m.Fjob = p.Fjob AND
    m.reason = p.reason AND
    m.guardian = p.guardian;

