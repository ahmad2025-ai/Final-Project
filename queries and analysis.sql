
-- creating G3_avg_all for both subjects
ALTER TABLE joined_student_data
ADD COLUMN G3_avg_all DECIMAL(5,2) NULL;


-- update the new column with combined average
SET SQL_SAFE_UPDATES = 0;

UPDATE joined_student_data
SET G3_avg_all = ROUND(
    (IFNULL(G1_math, 0) + IFNULL(G2_math, 0) + IFNULL(G3_math, 0) +
     IFNULL(G1_por, 0) + IFNULL(G2_por, 0) + IFNULL(G3_por, 0)) / 6.0, 2);

-- Optionally, re-enable safe updates after:
SET SQL_SAFE_UPDATES = 1;



-- Count of students by performance level based on combined average
SELECT
  CASE
    WHEN G3_avg_all >= 15 THEN 'High'
    WHEN G3_avg_all >= 10 THEN 'Medium'
    ELSE 'Low'
  END AS performance_level,
  COUNT(*) AS student_count
FROM joined_student_data
GROUP BY performance_level;


-- Students with combined average below passing grade
SELECT *
FROM joined_student_data
WHERE G3_avg_all < 10
ORDER BY G3_avg_all ASC;


-- populating g3 again and turning off the safe mode
SELECT
  G1_math, G2_math, G3_math,
  G1_por, G2_por, G3_por,
  ROUND((IFNULL(G1_math, 0) + IFNULL(G2_math, 0) + IFNULL(G3_math, 0) +
         IFNULL(G1_por, 0) + IFNULL(G2_por, 0) + IFNULL(G3_por, 0)) / 6.0, 2) AS test_avg
FROM joined_student_data
LIMIT 10;

SET SQL_SAFE_UPDATES = 0;

UPDATE joined_student_data
SET G3_avg_all = ROUND(
    (IFNULL(G1_math, 0) + IFNULL(G2_math, 0) + IFNULL(G3_math, 0) +
     IFNULL(G1_por, 0) + IFNULL(G2_por, 0) + IFNULL(G3_por, 0)) / 6.0, 2);

SELECT G3_avg_all FROM joined_student_data LIMIT 10;


-- performance level distribution
SELECT
  CASE
    WHEN G3_avg_all >= 15 THEN 'High'
    WHEN G3_avg_all >= 10 THEN 'Medium'
    ELSE 'Low'
  END AS performance_level,
  COUNT(*) AS student_count
FROM joined_student_data
GROUP BY performance_level;

-- average combined grade by gender
SELECT sex, ROUND(AVG(G3_avg_all), 2) AS avg_combined_grade
FROM joined_student_data
GROUP BY sex;

-- average combined grade by age
SELECT age, ROUND(AVG(G3_avg_all), 2) AS avg_grade_by_age
FROM joined_student_data
GROUP BY age
ORDER BY age;

-- student belwo passing grade
SELECT *
FROM joined_student_data
WHERE G3_avg_all < 10
ORDER BY G3_avg_all ASC;


-- add pass/Fail column
ALTER TABLE joined_student_data
ADD COLUMN pass_status VARCHAR(10);

UPDATE joined_student_data
SET pass_status = CASE
  WHEN G3_avg_all >= 10 THEN 'Pass'
  ELSE 'Fail'
END;

-- Pass/Fail Rate by Study Time
SELECT
  studytime_math AS study_time,
  pass_status,
  COUNT(*) AS count
FROM joined_student_data
GROUP BY study_time, pass_status
ORDER BY study_time, pass_status;

-- Pass/Fail Rate by Alcohol Use

SELECT
  (Dalc_math + Walc_math) / 2 AS avg_alcohol_use,
  pass_status,
  COUNT(*) AS count
FROM joined_student_data
GROUP BY avg_alcohol_use, pass_status
ORDER BY avg_alcohol_use;

-- or
SELECT
  CASE
    WHEN (Dalc_math + Walc_math)/2 >= 4 THEN 'Very High'
    WHEN (Dalc_math + Walc_math)/2 >= 3 THEN 'High'
    WHEN (Dalc_math + Walc_math)/2 >= 2 THEN 'Moderate'
    ELSE 'Low'
  END AS alcohol_level,
  pass_status,
  COUNT(*) AS count
FROM joined_student_data
GROUP BY alcohol_level, pass_status
ORDER BY alcohol_level;

-- Parental Education vs Performance
-- Mother's Education (Medu)
SELECT
  Medu AS mother_edu_level,
  pass_status,
  COUNT(*) AS count
FROM joined_student_data
GROUP BY Medu, pass_status
ORDER BY Medu;

-- Father's Education (Fedu)
SELECT
  Fedu AS father_edu_level,
  pass_status,
  COUNT(*) AS count
FROM joined_student_data
GROUP BY Fedu, pass_status
ORDER BY Fedu;

-- Absences vs Pass Rate
SELECT
  CASE
    WHEN absences_math + absences_por >= 30 THEN 'Very High (30+)'
    WHEN absences_math + absences_por >= 15 THEN 'High (15-29)'
    WHEN absences_math + absences_por >= 5 THEN 'Medium (5-14)'
    ELSE 'Low (0-4)'
  END AS absence_level,
  pass_status,
  COUNT(*) AS count
FROM joined_student_data
GROUP BY absence_level, pass_status
ORDER BY absence_level;

--  Pass/Fail Rate by School
SELECT
  school,
  pass_status,
  COUNT(*) AS student_count
FROM joined_student_data
GROUP BY school, pass_status
ORDER BY school, pass_status;

-- pass rate in %
SELECT
  school,
  ROUND(SUM(pass_status = 'Pass') / COUNT(*) * 100, 2) AS pass_rate_percent,
  ROUND(SUM(pass_status = 'Fail') / COUNT(*) * 100, 2) AS fail_rate_percent
FROM joined_student_data
GROUP BY school;

-- Performance by subject
-- Math
SELECT
  ROUND(AVG(G3_math), 2) AS avg_math_grade,
  ROUND(SUM(G3_math >= 10) / COUNT(*) * 100, 2) AS pass_rate_math,
  ROUND(SUM(G3_math < 10) / COUNT(*) * 100, 2) AS fail_rate_math
FROM joined_student_data;

-- Portuguese
SELECT
  ROUND(AVG(G3_por), 2) AS avg_por_grade,
  ROUND(SUM(G3_por >= 10) / COUNT(*) * 100, 2) AS pass_rate_por,
  ROUND(SUM(G3_por < 10) / COUNT(*) * 100, 2) AS fail_rate_por
FROM joined_student_data;

-- Mother's job vs Pass/Fail
SELECT
  Mjob,
  pass_status,
  COUNT(*) AS student_count
FROM joined_student_data
GROUP BY Mjob, pass_status
ORDER BY Mjob;

-- Father's Job vs Pass/Fail
SELECT
  Fjob,
  pass_status,
  COUNT(*) AS student_count
FROM joined_student_data
GROUP BY Fjob, pass_status
ORDER BY Fjob;

-- Combined Job Influence (Both Parents)
SELECT
  Mjob,
  Fjob,
  ROUND(AVG(G3_avg_all), 2) AS avg_grade,
  ROUND(SUM(pass_status = 'Pass') / COUNT(*) * 100, 2) AS pass_rate
FROM joined_student_data
GROUP BY Mjob, Fjob
ORDER BY avg_grade DESC;















