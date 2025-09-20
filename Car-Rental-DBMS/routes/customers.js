// routes/customers.js
const express = require("express");
const pool = require("../db");
const router = express.Router();

/**
 * GET /api/customers
 */
router.get("/", async (req, res) => {
  try {
    const [rows] = await pool.query("SELECT * FROM customers");
    res.json(rows);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Failed to fetch customers" });
  }
});

/** GET /api/customers/:id */
router.get("/:id", async (req, res) => {
  try {
    const [rows] = await pool.query("SELECT * FROM customers WHERE id = ?", [
      req.params.id,
    ]);
    if (!rows.length)
      return res.status(404).json({ error: "Customer not found" });
    res.json(rows[0]);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to fetch customer" });
  }
});

/** POST /api/customers */
router.post("/", async (req, res) => {
  try {
    const { first_name, last_name, email, phone, driver_license } = req.body;
    if (!first_name || !last_name || !email || !phone || !driver_license) {
      return res.status(400).json({ error: "Missing required fields" });
    }
    const [result] = await pool.query(
      `INSERT INTO customers (first_name, last_name, email, phone, driver_license) VALUES (?, ?, ?, ?, ?)`,
      [first_name, last_name, email, phone, driver_license]
    );
    // const [rows] = await pool.query('SELECT * FROM customers WHERE id = ?', [result.insertId]);
    // res.status(201).json(rows[0]);
    res
      .status(201)
      .json({ id: result.insertId, message: "Customer created successfully" });
  } catch (err) {
    console.error(err);
    if (err.code === "ER_DUP_ENTRY") {
      res
        .status(400)
        .json({ error: "Email, phone, or driver license already exists" });
    }
    res.status(500).json({ error: "Failed to create customer" });
  }
});

/** PUT /api/customers/:id */
router.put("/:id", async (req, res) => {
  try {
    const { first_name, last_name, email, phone, driver_license } = req.body;
    const [result] = await pool.query(
      `UPDATE customers SET first_name = ?, last_name = ?, email = ?, phone = ?, driver_license = ? WHERE id = ?`,
      [first_name, last_name, email, phone, driver_license, req.params.id]
    );
    if (result.affectedRows === 0)
      return res.status(404).json({ error: "Customer not found" });
    res.json({ message: "Customer updated successfully" });
  } catch (err) {
    console.error(err);
    if (err.code === "ER_DUP_ENTRY") {
      res
        .status(400)
        .json({ error: "Email, phone, or driver license already exists" });
    } else {
      res.status(500).json({ error: "Failed to update customer" });
    }
  }
});

/** DELETE /api/customers/:id */
router.delete("/:id", async (req, res) => {
  try {
    const [result] = await pool.query("DELETE FROM customers WHERE id = ?", [
      req.params.id,
    ]);
    if (result.affectedRows === 0) {
      return res.status(404).json({ error: "Customer not found" });
    }

    res.json({ message: "Customer deleted successfully" });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Failed to delete customer" });
  }
});

module.exports = router;
