
-- Thống kê số bệnh nhân theo tuổi, giới tính, tình trạng hôn nhân và thu nhập
INSERT OVERWRITE DIRECTORY '/user/fatcat/export_data/query1'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT 
    Age,
    Gender,
    MaritalStatus,
    AVG(IncomeFloat) AS AvgIncome,
    COUNT(*) AS TotalRecords
FROM temp_p_vr_data
GROUP BY Age, Gender, MaritalStatus
ORDER BY Age, Gender, MaritalStatus;

-- Thống kê số bệnh nhân theo giới tính, nghề nghiệp và tỷ lệ phần trăm
INSERT OVERWRITE DIRECTORY '/user/fatcat/export_data/query2'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT 
    Gender,
    Occupation,
    COUNT(*) AS Count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY Gender), 2) AS Percentage
FROM patients_fn
GROUP BY Gender, Occupation
ORDER BY Gender, Percentage DESC;

-- Phân tích số bệnh nhân phụ nữ con có độ tuổi từ 25 đến 35
INSERT OVERWRITE DIRECTORY '/user/fatcat/export_data/query3'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT 
    COUNT(*) AS WomenWithChildrenAged25To35
FROM patients_fn p
JOIN visit_records vr
    ON p.PatientID = vr.PatientID
WHERE 
    p.Gender = 'Female'
    AND p.NumberOfChildren > 0
    AND FLOOR(DATEDIFF(CURRENT_DATE, p.DateOfBirth) / 365.25) BETWEEN 25 AND 35

-- Số lượt khám theo từng năm, tình trạng sức khoẻ chung
INSERT OVERWRITE DIRECTORY '/user/fatcat/export_data/query4'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT 
    Year,
    GeneralHealthStatus,
    COUNT(VisitRecordID) AS VisitCount
FROM visit_records
GROUP BY Year, GeneralHealthStatus
ORDER BY Year, FIELD(GeneralHealthStatus, 'Good', 'Fair', 'Poor');

-- Thống kê điều kiện sống, mức độ hỗ trợ gia đình và mức độ căng thẳng tại nơi làm việc
INSERT OVERWRITE DIRECTORY '/user/fatcat/export_data/query5'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT 
    LivingConditions,
    FamilySupportLevel,
    WorkplaceStressLevel,
    COUNT(EnvironmentSocialRecordID) AS TotalVisit
FROM environment_social_fn
GROUP BY LivingConditions, FamilySupportLevel, WorkplaceStressLevel
ORDER BY TotalVisit DESC;

-- Thống kê 20 năm có số lượng bệnh nhân trầm cảm mức trung bình nhiều nhất
INSERT OVERWRITE DIRECTORY '/user/fatcat/export_data/query6'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT 
    Year,
    SUM(CASE 
            WHEN DepressionLevel = 'Low' THEN 0
            WHEN DepressionLevel = 'Medium' THEN 1
            WHEN DepressionLevel = 'High' THEN 0
            ELSE 0
        END) AS MediumDepressionCount
FROM temp_vr_onl_data
GROUP BY Year
ORDER BY MediumDepressionCount DESC
LIMIT 20;

-- Thống kê số bệnh nhân theo năm và mức độ căng thẳng, kiệt sức, trầm cảm
INSERT OVERWRITE DIRECTORY '/user/fatcat/export_data/query7'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT 
    Year,
    CASE StressLevel 
        WHEN 'Low' THEN 1
        WHEN 'Medium' THEN 2
        WHEN 'High' THEN 3
        ELSE NULL END AS StressLevel,
    CASE BurnoutLevel 
        WHEN 'Low' THEN 1
        WHEN 'Medium' THEN 2
        WHEN 'High' THEN 3
        ELSE NULL END AS BurnoutLevel,
    CASE DepressionLevel 
        WHEN 'Low' THEN 1
        WHEN 'Medium' THEN 2
        WHEN 'High' THEN 3
        ELSE NULL END AS DepressionLevel,
    COUNT(*) AS TotalVisit
FROM temp_vr_onl_data
GROUP BY Year, 
         CASE StressLevel 
             WHEN 'Low' THEN 1
             WHEN 'Medium' THEN 2
             WHEN 'High' THEN 3
             ELSE NULL END,
         CASE BurnoutLevel 
             WHEN 'Low' THEN 1
             WHEN 'Medium' THEN 2
             WHEN 'High' THEN 3
             ELSE NULL END,
         CASE DepressionLevel 
             WHEN 'Low' THEN 1
             WHEN 'Medium' THEN 2
             WHEN 'High' THEN 3
             ELSE NULL END
ORDER BY Year, StressLevel, BurnoutLevel, DepressionLevel;

-- Phân tích số bệnh nhân theo 1 số nước và giới tính
INSERT OVERWRITE DIRECTORY '/user/fatcat/export_data/query8'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT 
    c.Country,
    p.Gender,
    COUNT(PatientID) AS PatientCount
FROM contacts_fn c
JOIN patients_fn p
    ON c.ContactID = p.ContactID
GROUP BY c.Country, p.Gender
ORDER BY c.Country, PatientCount DESC;

-- Thống kê tỉ lệ số bệnh nhân có 3 mức độ căng thẳng, kiệt sức, trầm cảm cao nhất
INSERT OVERWRITE DIRECTORY '/user/fatcat/export_data/query9'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT 
    Year,
    COUNT(CASE 
            WHEN StressLevel = 'High' AND BurnoutLevel = 'High' AND DepressionLevel = 'High' THEN 1 
            ELSE NULL 
        END) * 100.0 / COUNT(*) AS HighAllPercentage
FROM temp_vr_env_data
GROUP BY Year
ORDER BY Year;

-- Phân tích xem 1 số các yếu tố ảnh hưởng đến Thói quen ngủ
INSERT OVERWRITE DIRECTORY '/user/fatcat/export_data/query10'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT SocialMediaUsage, WorkingHours, GamingFrequency, SleepPatterns, COUNT(HealthHabitsRecordID) AS Count
FROM health_habits_fn
GROUP BY SocialMediaUsage, WorkingHours, GamingFrequency, SleepPatterns;