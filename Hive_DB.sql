CREATE TABLE patients_fn (
    PatientID INT,
    FullName STRING,
    DateOfBirth DATE,
    MaritalStatus STRING,
    EducationLevel STRING,
    NumberOfChildren INT,
    Occupation STRING,
    Income STRING,
    ContactID INT,
    Gender STRING
)
CLUSTERED BY (PatientID) INTO 20 BUCKETS
STORED AS PARQUET;

CREATE TABLE visit_records (
    VisitRecordID INT,
    PatientID INT,
    HealthHabitRecordID INT,
    MentalAssessmentRecordID INT,
    MentalHealthRecordID INT,
    DigitalBehaviorRecordID INT,
    EnvironmentSocialRecordID INT,
    MedicalHistoryRecordID INT,
    VisitDate DATE,
    GeneralHealthStatus STRING,
    Notes STRING,
    Year INT
)
CLUSTERED BY (PatientID) INTO 20 BUCKETS
STORED AS PARQUET;

CREATE TABLE contacts_fn (
    ContactID INT,
    PhoneNumber STRING,
    Email STRING,
    Address STRING,
    City STRING,
    Country STRING
)
CLUSTERED BY (ContactID) INTO 20 BUCKETS
STORED AS PARQUET;

CREATE TABLE health_habits_fn (
    HealthHabitsRecordID INT,
    SmokingStatus STRING,
    PhysicalActivityLevel STRING,
    AlcoholConsumption STRING,
    DietaryHabits STRING,
    SleepPatterns STRING,
    SocialMediaUsage STRING,
    WorkingHours INT,
    GamingFrequency STRING
)
CLUSTERED BY (HealthHabitsRecordID) INTO 20 BUCKETS
STORED AS PARQUET;

CREATE TABLE mental_assessment_fn (
    MentalAssessmentRecordID INT,
    AnxietyLevel STRING,
    BurnoutLevel STRING,
    DepressionLevel STRING,
    StressLevel STRING,
    SelfEsteemLevel STRING
)
CLUSTERED BY (MentalAssessmentRecordID) INTO 20 BUCKETS
STORED AS PARQUET;

CREATE TABLE mental_health_fn (
    MentalHealthRecordID INT,
    TreatmentType STRING,
    TherapySessionsCount STRING,
    SeverityLevelOfDiagnosis STRING,
    TraumaHistory STRING,
    MedicationAdherence STRING,
    RelapseHistory STRING,
    MentalHealthDiagnosis STRING
)
CLUSTERED BY (MentalHealthRecordID) INTO 20 BUCKETS
STORED AS PARQUET;

CREATE TABLE digital_activity_fn (
    DigitalBehaviorRecordID INT,
    VirtualCommunicationFrequency STRING,
    DigitalDetoxFrequency STRING,
    OnlineParticipation STRING,
    SocialMediaAddictionLevel STRING
)
CLUSTERED BY (DigitalBehaviorRecordID) INTO 20 BUCKETS
STORED AS PARQUET;

CREATE TABLE environment_social_fn (
    EnvironmentSocialRecordID INT,
    LivingConditions STRING,
    CommunityEngagement STRING,
    PeerPressureLevel STRING,
    WorkLifeBalance STRING,
    ExposureToNews STRING,
    FamilySupportLevel STRING,
    WorkplaceStressLevel STRING
)
CLUSTERED BY (EnvironmentSocialRecordID) INTO 20 BUCKETS
STORED AS PARQUET;

-- Temporary tables for data storage
CREATE TABLE temp_p_vr_data STORED AS PARQUET AS
SELECT 
    hv.VisitRecordID,
    hv.PatientID,
    hv.Year,
    hv.VisitDate,
    FLOOR(DATEDIFF(CURRENT_DATE, p.DateOfBirth) / 365.25) AS Age,
    p.Gender,
    p.MaritalStatus,
    CAST(REGEXP_REPLACE(p.Income, '[$,]', '') AS FLOAT) AS IncomeFloat,
    p.Occupation,
    p.ContactID,
    p.NumberOfChildren
FROM hospital_visit_records hv
LEFT JOIN patients p ON hv.PatientID = p.PatientID;

CREATE TABLE temp_visit_records_data STORED AS PARQUET AS
SELECT 
    hv.VisitRecordID,
    hv.PatientID,
    hv.Year,
    hv.VisitDate,
    ma.StressLevel,
    ma.BurnoutLevel,
    ma.DepressionLevel,
    h.SleepPatterns,
    h.PhysicalActivityLevel,
    h.AlcoholConsumption,
    h.DietaryHabits,
    h.WorkingHours,
    da.OnlineParticipation,
    es.PeerPressureLevel,
    es.LivingConditions
FROM visit_records hv
LEFT JOIN mental_assessment_fn ma 
    ON hv.MentalAssessmentRecordID = ma.MentalAssessmentRecordID
LEFT JOIN health_habits_fn h 
    ON hv.HealthHabitRecordID = h.HealthHabitsRecordID;
-- null values in the table

CREATE TABLE temp_vr_env_data STORED AS PARQUET AS
SELECT 
    hv.VisitRecordID,
    hv.PatientID,
    hv.Year,
    hv.VisitDate,
    ma.StressLevel,
    ma.BurnoutLevel,
    ma.DepressionLevel,
    es.PeerPressureLevel,
    es.LivingConditions
FROM visit_records hv
LEFT JOIN mental_assessment_fn ma 
    ON hv.MentalAssessmentRecordID = ma.MentalAssessmentRecordID
LEFT JOIN environment_social_fn es 
    ON hv.EnvironmentSocialRecordID = es.EnvironmentSocialRecordID;
-- null values in the table 2 last columns


CREATE TABLE temp_vr_onl_data STORED AS PARQUET AS
SELECT 
    hv.VisitRecordID,
    hv.PatientID,
    hv.Year,
    hv.VisitDate,
    ma.StressLevel,
    ma.BurnoutLevel,
    ma.DepressionLevel,
    da.OnlineParticipation
FROM visit_records hv
LEFT JOIN mental_assessment_fn ma 
    ON hv.MentalAssessmentRecordID = ma.MentalAssessmentRecordID
LEFT JOIN digital_activity_fn da 
    ON hv.DigitalBehaviorRecordID = da.DigitalBehaviorRecordID;
-- null last column
