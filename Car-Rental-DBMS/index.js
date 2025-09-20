// index.js
const express = require('express');
const bodyParser = require('body-parser');
const dotenv = require('dotenv');
dotenv.config();

const customersRouter = require('./routes/customers');
const vehiclesRouter = require('./routes/vehicles');

const app = express();
app.use(bodyParser.json());

app.use('/api/customers', customersRouter);
app.use('/api/vehicles', vehiclesRouter);

// health
app.get('/', (req, res) => res.json({ message: 'Car Rental API is running' }));

const PORT = process.env.PORT || 8000;
app.listen(PORT, () => console.log(`Server listening on port ${PORT}`));
