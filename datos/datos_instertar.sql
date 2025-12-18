CREATE DATABASE IF NOT EXISTS evaluacion_u3_poo
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

USE evaluacion_u3_poo;

CREATE TABLE IF NOT EXISTS usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL UNIQUE,
  email VARCHAR(191) NOT NULL,
  password_hash CHAR(64) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY uq_usuarios_email (email)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS posts (
  id INT PRIMARY KEY,
  userId INT NOT NULL,
  title VARCHAR(255) NOT NULL,
  body TEXT NOT NULL
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS comments (
  id INT PRIMARY KEY,
  postId INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(191) NOT NULL,
  body TEXT NOT NULL,
  INDEX idx_comments_postId (postId),
  CONSTRAINT fk_comments_posts
    FOREIGN KEY (postId) REFERENCES posts(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE=InnoDB;
