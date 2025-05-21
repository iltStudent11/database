-- Customer Table
CREATE TABLE Customer (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Phone VARCHAR(50)
);

-- Address Table
CREATE TABLE Address (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    CustomerId INT NOT NULL,
    Street1 VARCHAR(255) NOT NULL,
    Street2 VARCHAR(255),
    City VARCHAR(100) NOT NULL,
    State VARCHAR(100) NOT NULL,
    Country VARCHAR(100) NOT NULL,
    ZIP VARCHAR(20) NOT NULL,
    FOREIGN KEY (CustomerId) REFERENCES Customer(Id)
);

-- Product Table
CREATE TABLE Product (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    Price INT NOT NULL
);

-- CustomerOrder Table
CREATE TABLE CustomerOrder (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    CustomerId INT NOT NULL,
    ProductId INT NOT NULL,
    Quantity INT NOT NULL,
    ShippingAddressId INT NOT NULL,
    CreationDte DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Status ENUM('Placed', 'Shipped', 'Cancelled') NOT NULL,
    FOREIGN KEY (CustomerId) REFERENCES Customer(Id),
    FOREIGN KEY (ProductId) REFERENCES Product(Id),
    FOREIGN KEY (ShippingAddressId) REFERENCES Address(Id)
);
