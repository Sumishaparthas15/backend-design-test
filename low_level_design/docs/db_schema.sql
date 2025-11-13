-- db_schema.sql
-- Users table (Django default simplified)
CREATE TABLE auth_user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    email VARCHAR(254),
    password VARCHAR(128) NOT NULL,
    is_staff BOOLEAN DEFAULT FALSE,
    is_superuser BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Translation jobs table
CREATE TABLE translation_job (
    id UUID PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES auth_user (id) ON DELETE CASCADE,
    source_text TEXT,
    source_lang VARCHAR(10) NOT NULL,
    target_lang VARCHAR(10) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    priority VARCHAR(10) NOT NULL DEFAULT 'normal',
    word_count INTEGER DEFAULT 0,
    translated_text TEXT,
    error_message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    started_at TIMESTAMP,
    completed_at TIMESTAMP
);

-- Indexes for common queries
CREATE INDEX idx_translationjob_status ON translation_job (status);
CREATE INDEX idx_translationjob_priority ON translation_job (priority);
CREATE INDEX idx_translationjob_created_at ON translation_job (created_at);

-- Optional: queue metadata table (helps autoscaling / monitoring)
CREATE TABLE translation_queue (
    id SERIAL PRIMARY KEY,
    job_id UUID NOT NULL REFERENCES translation_job (id) ON DELETE CASCADE,
    queue_name VARCHAR(50) NOT NULL,
    enqueued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    processed BOOLEAN DEFAULT FALSE
);
