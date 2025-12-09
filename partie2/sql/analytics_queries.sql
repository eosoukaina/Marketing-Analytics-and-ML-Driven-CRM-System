-- ============================================
-- Exercice 2.1.1 : Requêtes SQL Analytics
-- TP03 - Web Marketing & CRM
-- Auteur: Hind Abida 
-- ============================================

-- ============================================
-- SCHÉMA DE BASE DE DONNÉES
-- ============================================

-- Table des événements
CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    user_id VARCHAR(50),
    event_type VARCHAR(50), -- 'page_view', 'add_to_cart', 'purchase'
    timestamp TIMESTAMP DEFAULT NOW(),
    channel VARCHAR(50), -- 'organic', 'paid', 'email', 'social'
    revenue DECIMAL(10,2) DEFAULT 0,
    properties JSONB -- données additionnelles
);

-- Table des sessions
CREATE TABLE sessions (
    session_id VARCHAR(50) PRIMARY KEY,
    user_id VARCHAR(50),
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    pages_viewed INT DEFAULT 0,
    converted BOOLEAN DEFAULT FALSE,
    channel VARCHAR(50)
);

-- Index pour la performance
CREATE INDEX idx_events_user ON events(user_id);
CREATE INDEX idx_events_type ON events(event_type);
CREATE INDEX idx_sessions_user ON sessions(user_id);
CREATE INDEX idx_events_timestamp ON events(timestamp);
CREATE INDEX idx_sessions_start ON sessions(start_time);

-- ============================================
-- INSERTION DE DONNÉES DE TEST
-- ============================================

-- Insertion d'événements de test
INSERT INTO events (user_id, event_type, channel, revenue, timestamp) VALUES
('user_001', 'page_view', 'organic', 0, '2025-01-15 10:00:00'),
('user_001', 'add_to_cart', 'organic', 0, '2025-01-15 10:05:00'),
('user_001', 'purchase', 'organic', 150.00, '2025-01-15 10:10:00'),
('user_002', 'page_view', 'paid', 0, '2025-01-15 11:00:00'),
('user_002', 'page_view', 'paid', 0, '2025-01-15 11:05:00'),
('user_003', 'page_view', 'email', 0, '2025-01-15 12:00:00'),
('user_003', 'add_to_cart', 'email', 0, '2025-01-15 12:10:00'),
('user_003', 'purchase', 'email', 250.00, '2025-01-15 12:20:00'),
('user_004', 'page_view', 'social', 0, '2025-01-15 13:00:00'),
('user_005', 'page_view', 'organic', 0, '2025-01-15 14:00:00'),
('user_005', 'purchase', 'organic', 75.00, '2025-01-15 14:15:00'),
('user_006', 'page_view', 'paid', 0, '2025-01-15 15:00:00'),
('user_006', 'add_to_cart', 'paid', 0, '2025-01-15 15:10:00'),
('user_006', 'purchase', 'paid', 320.00, '2025-01-15 15:20:00'),
('user_007', 'page_view', 'email', 0, '2025-01-15 16:00:00'),
('user_008', 'page_view', 'social', 0, '2025-01-15 17:00:00'),
('user_008', 'purchase', 'social', 180.00, '2025-01-15 17:30:00'),
('user_009', 'page_view', 'organic', 0, '2025-01-15 18:00:00'),
('user_010', 'page_view', 'paid', 0, '2025-01-15 19:00:00');

-- Insertion de sessions de test
INSERT INTO sessions (session_id, user_id, start_time, end_time, pages_viewed, converted, channel) VALUES
('sess_001', 'user_001', '2025-01-15 10:00:00', '2025-01-15 10:15:00', 5, TRUE, 'organic'),
('sess_002', 'user_002', '2025-01-15 11:00:00', '2025-01-15 11:10:00', 2, FALSE, 'paid'),
('sess_003', 'user_003', '2025-01-15 12:00:00', '2025-01-15 12:25:00', 7, TRUE, 'email'),
('sess_004', 'user_004', '2025-01-15 13:00:00', '2025-01-15 13:05:00', 1, FALSE, 'social'),
('sess_005', 'user_005', '2025-01-15 14:00:00', '2025-01-15 14:20:00', 3, TRUE, 'organic'),
('sess_006', 'user_006', '2025-01-15 15:00:00', '2025-01-15 15:25:00', 6, TRUE, 'paid'),
('sess_007', 'user_007', '2025-01-15 16:00:00', '2025-01-15 16:05:00', 1, FALSE, 'email'),
('sess_008', 'user_008', '2025-01-15 17:00:00', '2025-01-15 17:35:00', 4, TRUE, 'social'),
('sess_009', 'user_009', '2025-01-15 18:00:00', '2025-01-15 18:08:00', 2, FALSE, 'organic'),
('sess_010', 'user_010', '2025-01-15 19:00:00', '2025-01-15 19:05:00', 1, FALSE, 'paid'),
('sess_011', 'user_006', '2025-01-15 15:00:00', '2025-01-15 15:30:00', 6, TRUE, 'paid'),
('sess_012', 'user_007', '2025-01-15 16:00:00', '2025-01-15 16:35:00', 1, FALSE, 'email'),
('sess_013', 'user_008', '2025-01-15 17:00:00', '2025-01-15 18:25:00', 4, TRUE, 'social'),
('sess_014', 'user_009', '2025-01-15 18:00:00', '2025-01-15 19:08:00', 2, FALSE, 'organic'),
('sess_015', 'user_010', '2025-01-15 19:00:00', '2025-01-15 20:05:00', 1, FALSE, 'paid');

-- ============================================
-- REQUÊTE 1 : TAUX DE CONVERSION PAR CANAL
-- ============================================

-- Version fournie dans le TP
SELECT 
    channel,
    COUNT(DISTINCT CASE WHEN converted THEN user_id END) * 100.0 / 
    COUNT(DISTINCT user_id) AS conversion_rate
FROM sessions
GROUP BY channel
ORDER BY conversion_rate DESC;

-- votre version 


-- ============================================
-- REQUÊTE 2 : REVENU MOYEN PAR UTILISATEUR (ARPU)
-- ============================================

-- ARPU global (Average Revenue Per User)
SELECT 
    ROUND(AVG(user_revenue), 2) AS arpu
FROM (
    SELECT 
        user_id,
        SUM(revenue) AS user_revenue
    FROM events
    WHERE event_type = 'purchase'
    GROUP BY user_id
) AS user_revenues;

-- ARPU par canal
SELECT 
    channel,
    ROUND(AVG(user_revenue), 2) AS arpu,
    COUNT(DISTINCT user_id) AS total_users,
    SUM(user_revenue) AS total_revenue
FROM (
    SELECT 
        e.user_id,
        e.channel,
        SUM(e.revenue) AS user_revenue
    FROM events e
    WHERE e.event_type = 'purchase'
    GROUP BY e.user_id, e.channel
) AS user_channel_revenue
GROUP BY channel
ORDER BY arpu DESC;




-- ============================================
-- REQUÊTE 3 : TOP 5 DES HEURES AVEC LE MEILLEUR TAUX DE CONVERSION
-- ============================================

-- Méthode 1 : Basée sur les sessions
SELECT 
    EXTRACT(HOUR FROM start_time) AS hour_of_day,
    COUNT(*) AS total_sessions,
    SUM(CASE WHEN converted THEN 1 ELSE 0 END) AS conversions,
    ROUND(
        SUM(CASE WHEN converted THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS conversion_rate
FROM sessions
GROUP BY EXTRACT(HOUR FROM start_time)
HAVING COUNT(*) >= 1  -- Au moins 1 session pour être significatif
ORDER BY conversion_rate DESC, total_sessions DESC
LIMIT 5;

-- Méthode 2 : Basée sur les événements d'achat
SELECT 
    EXTRACT(HOUR FROM timestamp) AS hour_of_day,
    COUNT(DISTINCT user_id) AS unique_visitors,
    SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS purchases,
    ROUND(
        SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) * 100.0 / 
        COUNT(DISTINCT user_id),
        2
    ) AS conversion_rate
FROM events
GROUP BY EXTRACT(HOUR FROM timestamp)
ORDER BY conversion_rate DESC
LIMIT 5;


-- ============================================
--  REQUÊTE 4 : COHORT ANALYSIS - Rétention des utilisateurs par mois d'inscription
-- ============================================

-- Note: Pour une vraie cohort analysis, nous aurions besoin d'une table users avec date_inscription
-- Ici, nous simulons avec la première interaction de chaque utilisateur

-- Étape 1 : Identifier le mois de première activité (cohorte) de chaque utilisateur
WITH user_cohorts AS (
    SELECT 
        user_id,
        DATE_TRUNC('month', MIN(timestamp)) AS cohort_month
    FROM events
    GROUP BY user_id
),

-- Étape 2 : Calculer l'activité mensuelle de chaque utilisateur
user_activity AS (
    SELECT 
        e.user_id,
        uc.cohort_month,
        DATE_TRUNC('month', e.timestamp) AS activity_month,
        -- Mois depuis inscription (0 = mois d'inscription, 1 = mois suivant, etc.)
        EXTRACT(YEAR FROM AGE(DATE_TRUNC('month', e.timestamp), uc.cohort_month)) * 12 +
        EXTRACT(MONTH FROM AGE(DATE_TRUNC('month', e.timestamp), uc.cohort_month)) AS months_since_cohort
    FROM events e
    JOIN user_cohorts uc ON e.user_id = uc.user_id
    GROUP BY e.user_id, uc.cohort_month, DATE_TRUNC('month', e.timestamp)
),

-- Étape 3 : Calculer la rétention par cohorte et par mois
cohort_retention AS (
    SELECT 
        cohort_month,
        months_since_cohort,
        COUNT(DISTINCT user_id) AS active_users
    FROM user_activity
    GROUP BY cohort_month, months_since_cohort
),

-- Étape 4 : Taille initiale de chaque cohorte
cohort_sizes AS (
    SELECT 
        cohort_month,
        COUNT(DISTINCT user_id) AS cohort_size
    FROM user_cohorts
    GROUP BY cohort_month
)

-- Résultat final : Taux de rétention par cohorte
SELECT 
    TO_CHAR(cr.cohort_month, 'YYYY-MM') AS cohort,
    cs.cohort_size AS initial_users,
    cr.months_since_cohort AS month_number,
    cr.active_users,
    ROUND(cr.active_users * 100.0 / cs.cohort_size, 2) AS retention_rate
FROM cohort_retention cr
JOIN cohort_sizes cs ON cr.cohort_month = cs.cohort_month
ORDER BY cr.cohort_month, cr.months_since_cohort;

-- Version simplifiée : Rétention globale par mois depuis inscription
WITH user_cohorts AS (
    SELECT 
        user_id,
        MIN(timestamp) AS first_seen
    FROM events
    GROUP BY user_id
)
SELECT 
    EXTRACT(MONTH FROM AGE(e.timestamp, uc.first_seen)) AS months_since_first_visit,
    COUNT(DISTINCT e.user_id) AS active_users,
    ROUND(
        COUNT(DISTINCT e.user_id) * 100.0 / 
        (SELECT COUNT(DISTINCT user_id) FROM user_cohorts),
        2
    ) AS retention_percentage
FROM events e
JOIN user_cohorts uc ON e.user_id = uc.user_id
GROUP BY EXTRACT(MONTH FROM AGE(e.timestamp, uc.first_seen))
ORDER BY months_since_first_visit;
