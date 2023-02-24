CREATE TABLE users (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(50) UNIQUE NOT NULL,
  password VARCHAR(100) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
  role ENUM('driver', 'mechanic') NOT NULL DEFAULT 'driver'
);

CREATE TABLE vehicles (
  id INT PRIMARY KEY,
  user_id INT NOT NULL,
  brand VARCHAR(50) NOT NULL,
  model VARCHAR(50) NOT NULL,
  license_plate VARCHAR(10) NOT NULL,
  color VARCHAR(20),
  year INT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE services (
  id INT PRIMARY KEY,
  driver_id INT NOT NULL,
  mechanic_id INT NOT NULL,
  vehicle_id INT NOT NULL,
  location VARCHAR(200) NOT NULL,
  description VARCHAR(400) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  role ENUM('running', 'unsolved', 'solved') NOT NULL DEFAULT 'running',
  FOREIGN KEY (driver_id) REFERENCES users(id),
  FOREIGN KEY (mechanic_id) REFERENCES users(id),
  FOREIGN KEY (vehicle_id) REFERENCES vehicles(id)
);
