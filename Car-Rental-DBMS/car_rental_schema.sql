-- car_rental_schema.sql
-- Single SQL file: creates database, tables, constraints, indexes.

DROP DATABASE IF EXISTS car_rental;
CREATE DATABASE car_rental CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE car_rental;

-- Customers table
CREATE TABLE customers (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  phone VARCHAR(30) NOT NULL UNIQUE,
  driver_license VARCHAR(100) NOT NULL UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Vehicles table
CREATE TABLE vehicles (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  plate_number VARCHAR(30) NOT NULL UNIQUE,
  make VARCHAR(100) NOT NULL,
  model VARCHAR(100) NOT NULL,
  year YEAR NOT NULL,
  category ENUM('economy','compact','midsize','suv','luxury','van','truck') DEFAULT 'economy',
  status ENUM('available','rented','maintenance','reserved') DEFAULT 'available',
  daily_rate DECIMAL(10,2) NOT NULL DEFAULT 0.00,
  mileage INT UNSIGNED DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Rentals table (one customer can have many rentals; one vehicle can be rented many times over time)
CREATE TABLE rentals (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  customer_id INT UNSIGNED NOT NULL,
  vehicle_id INT UNSIGNED NOT NULL,
  pickup_location VARCHAR(255) NOT NULL,
  dropoff_location VARCHAR(255) DEFAULT NULL,
  start_date DATETIME NOT NULL,
  end_date DATETIME NOT NULL,
  total_amount DECIMAL(12,2) NOT NULL DEFAULT 0.00,
  status ENUM('reserved','ongoing','completed','cancelled') DEFAULT 'reserved',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT fk_rentals_customer FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT fk_rentals_vehicle FOREIGN KEY (vehicle_id) REFERENCES vehicles(id) ON DELETE RESTRICT ON UPDATE CASCADE,
  CHECK (end_date > start_date)
) ENGINE=InnoDB;

-- Payments table (many payments can belong to a rental)
CREATE TABLE payments (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  rental_id INT UNSIGNED NOT NULL,
  amount DECIMAL(12,2) NOT NULL,
  method ENUM('cash','card','mpesa','bank_transfer','other') DEFAULT 'card',
  paid_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  receipt_number VARCHAR(150),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_payments_rental FOREIGN KEY (rental_id) REFERENCES rentals(id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- Amenities and many-to-many between vehicles and amenities
CREATE TABLE amenities (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL UNIQUE,
  description VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE vehicle_amenities (
  vehicle_id INT UNSIGNED NOT NULL,
  amenity_id INT UNSIGNED NOT NULL,
  PRIMARY KEY (vehicle_id, amenity_id),
  CONSTRAINT fk_va_vehicle FOREIGN KEY (vehicle_id) REFERENCES vehicles(id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_va_amenity FOREIGN KEY (amenity_id) REFERENCES amenities(id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- Useful indexes (Improves database performance for common queries)
CREATE INDEX idx_rentals_customer ON rentals(customer_id);
CREATE INDEX idx_rentals_vehicle ON rentals(vehicle_id);
CREATE INDEX idx_vehicle_status ON vehicles(status);
CREATE INDEX idx_payments_rental ON payments(rental_id);

-- Seed some sample data (optional)
INSERT INTO amenities (name, description) VALUES
('GPS', 'GPS Navigation'),
('Child Seat', 'Child safety seat'),
('Bluetooth', 'Bluetooth audio'),
('All Wheel Drive', 'AWD');

INSERT INTO vehicles (plate_number, make, model, year, category, status, daily_rate, mileage)
VALUES
('KAA-001A','Toyota','Corolla','2019','compact','available', 40.00, 42000),
('KBB-234B','Range Rover','Sport','2021','luxury','available', 200.00, 15000),
('KCC-999C','Mercedes','C300','2020','luxury','maintenance', 180.00, 30000);

INSERT INTO customers (first_name,last_name,email,phone,driver_license)
VALUES
('Mwamuye','Joseph','mwamuye@example.com','+254700000000','DL987654321'),
('Aisha','Kariuki','aisha.k@example.com','+254711111111','DL123456789');

-- Attach amenities to a vehicle
INSERT INTO vehicle_amenities (vehicle_id, amenity_id) VALUES (1,1),(1,3),(2,1),(2,3),(2,4);

-- Example rental
INSERT INTO rentals (customer_id, vehicle_id, pickup_location, dropoff_location, start_date, end_date, total_amount, status)
VALUES (1,1,'Nairobi Office','Nairobi Office','2025-09-20 09:00:00','2025-09-25 09:00:00', 200.00, 'reserved');

-- End of schema
