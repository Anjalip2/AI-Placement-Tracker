CREATE DATABASE placement_tracker;

USE placement_tracker;

CREATE TABLE students (
    usn VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    branch VARCHAR(50) NOT NULL,
    cgpa DECIMAL(3,2) NOT NULL
);