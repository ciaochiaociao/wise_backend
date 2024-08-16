-- not available in PostgreSQL
-- DROP DATABASE IF EXISTS wise;
-- CREATE DATABASE wise;

-- Create the Emotion table with appropriate data types

BEGIN;
DROP TABLE IF EXISTS emotion, emotion_record;
CREATE TABLE IF NOT EXISTS emotion (
  id SMALLSERIAL PRIMARY KEY,  -- 1 btye
  name VARCHAR(12) NOT NULL UNIQUE  -- 12 + 1 length bytes
);
CREATE INDEX name_index ON emotion USING HASH (name);  -- O(1) time, O(n) space

-- Insert initial emotion data into the Emotion table
INSERT INTO emotion (name) VALUES 
('happy'), 
('sad'), 
('angry'), 
('surprised'), 
('disgusted'), 
('fearful'), 
('neutral');
-- CREATE TYPE Emotion AS ENUM ('happy', 'sad', 'angry', 'surprised', 'disgusted', 'fearful', 'neutral');

-- Create the EmotionLog table with a foreign key reference to the Emotion table
CREATE TABLE IF NOT EXISTS emotion_record (
    id SERIAL PRIMARY KEY,
    -- emotion emotion,
    emotion_id SMALLINT NOT NULL,
    confidence REAL NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT LOCALTIMESTAMP,
    FOREIGN KEY (emotion_id) REFERENCES Emotion(Id)
    -- INDEX (emotion_id)
);

-- Create indexes on the EmotionLog table to improve query performance
-- O(log n) time for balanced tree insertion
CREATE INDEX created_at_index ON emotion_record USING BTREE (created_at);
CREATE INDEX emotion_id_index ON emotion_record USING BTREE (emotion_id);

COMMIT;

BEGIN;
-- Create the fake data for the EmotionLog table
INSERT INTO emotion_record (emotion_id, confidence, created_at) VALUES 
(1, 0.9637, '2024-08-01 09:02:10.130632'),
(2, 0.8780, '2024-08-01 09:02:11.003355'),
(1, 0.9910, '2024-08-01 09:02:12.100113'),
(1, 0.7792, '2024-08-01 09:02:12.200113'),
(2, 0.8901, '2024-08-01 09:02:13.300113'),
(3, 0.9811, '2024-08-01 09:02:13.400113'),
(1, 0.7779, '2024-08-01 09:02:13.500113'),
(4, 0.6903, '2024-08-01 09:02:14.600113'),
(6, 0.6100, '2024-08-01 09:02:15.700113'),
(5, 0.8132, '2024-08-01 09:02:16.800113'),
(3, 0.6168, '2024-08-01 09:02:16.900113'),
(4, 0.7862, '2024-08-01 09:02:17.000113');
COMMIT;