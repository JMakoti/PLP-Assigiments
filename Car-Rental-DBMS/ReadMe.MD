
# Car Rental Management System

A Node.js RESTful API for managing vehicles and customers in a car rental business. This project provides endpoints for CRUD operations and uses a MySQL database for data storage.


## Features

- **Vehicle Management**: Create, read, update, and delete vehicle records
- **Customer Management**: Create, read, update, and delete customer records
- **RESTful API**: Clean API endpoints for integration with other applications
- **MySQL Database**: Robust data storage with proper relationships and constraints


## Prerequisites

Before running this application, make sure you have the following installed:

- Node.js (version 14 or higher)
- MySQL (version 5.7 or higher)
- npm (usually comes with Node.js)


## Installation

1. **Clone or download the project files** to your local machine.

2. **Navigate to the project directory**:
   ```bash
   cd Car-Rental-DBMS
   ```

3. **Install the dependencies**:
   ```bash
   npm install
   ```

4. **Set up the MySQL database**:
   - Open MySQL command line or a database management tool
   - Run the SQL commands from the `car_rental_schema.sql` file to create the database and tables

5. **Configure the database connection**:
   - Copy `.env.sample` to `.env` and update the values with your MySQL credentials:
     ```env
     DB_HOST=localhost
     DB_PORT=3306
     DB_USER=your_mysql_username
     DB_PASSWORD=your_mysql_password
     DB_NAME=car_rental
     PORT=8000
     ```


## Running the Application

1. **Start the server**:
   ```bash
   npm start
   ```
   For development with auto-restart on changes:
   ```bash
   npm run dev
   ```

2. **Test the API**
   - The server will run on the port specified in your `.env` file (default: 8000).
   - You can test the API using tools like Postman or curl:
     ```bash
     curl http://localhost:8000/api/vehicles
     ```


## API Endpoints

### Vehicles

- `GET /api/vehicles` - Get all vehicles
- `GET /api/vehicles/:id` - Get a specific vehicle by ID
- `POST /api/vehicles` - Create a new vehicle
- `PUT /api/vehicles/:id` - Update a vehicle
- `DELETE /api/vehicles/:id` - Delete a vehicle

### Customers

- `GET /api/customers` - Get all customers
- `GET /api/customers/:id` - Get a specific customer by ID
- `POST /api/customers` - Create a new customer
- `PUT /api/customers/:id` - Update a customer
- `DELETE /api/customers/:id` - Delete a customer


## Usage

This project provides a backend API only. You can use Postman, curl, or integrate with a frontend to manage vehicles and customers. Example request to add a vehicle:

```bash
curl -X POST http://localhost:8000/api/vehicles \
   -H "Content-Type: application/json" \
   -d '{
      "plate_number": "KDD-123D",
      "make": "Nissan",
      "model": "Note",
      "year": 2022,
      "category": "compact",
      "status": "available",
      "daily_rate": 50.00,
      "mileage": 10000
   }'
```


## Project Structure

```
Car-Rental-DBMS/
├── index.js            # Main application file (Express server)
├── db.js               # Database connection configuration
├── routes/
│   ├── vehicles.js     # API routes for vehicle operations
│   └── customers.js    # API routes for customer operations
├── car_rental_schema.sql # SQL schema for database setup
├── .env.sample         # Example environment config
├── package.json        # Project metadata and dependencies
└── ReadMe.MD           # Project documentation
```


## Database Schema

See `car_rental_schema.sql` for full details. Main tables:

- **vehicles**: Stores information about rental cars
- **customers**: Stores information about customers
- **rentals**: Links customers to vehicles they've rented
- **payments**: Records payments for rentals
- **amenities**: Stores available vehicle amenities
- **vehicle_amenities**: Junction table linking vehicles to amenities


## Troubleshooting

1. **Database Connection Issues**:
   - Verify your MySQL server is running
   - Check your database credentials in `.env`
   - Ensure the `car_rental` database exists

2. **Port Already in Use**:
   - Change the `PORT` value in your `.env` file if the default port is in use

3. **Dependency Issues**:
   - Delete `node_modules` folder and run `npm install` again


## Next Steps for Enhancement

- Implement edit functionality for both vehicles and customers
- Add rental management features
- Implement payment processing
- Add user authentication and authorization
- Add a frontend interface
- Add search and filtering capabilities
- Implement input validation and sanitization


## License

This project is open source and available under the MIT License.