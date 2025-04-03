CREATE TABLE IF NOT EXISTS city (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    population INTEGER
);

-- Insert sample cities
INSERT INTO city (name, country, population) VALUES
    ('New York', 'USA', 8804190),
    ('Tokyo', 'Japan', 13929286),
    ('London', 'UK', 8982000),
    ('Paris', 'France', 2161000),
    ('Sydney', 'Australia', 5312000);