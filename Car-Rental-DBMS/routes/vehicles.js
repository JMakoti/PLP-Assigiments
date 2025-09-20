// routes/vehicles.js
const express = require("express");
const pool = require("../db");
const router = express.Router();

/** GET /api/vehicles */
router.get("/", async (req, res) => {
  try {
    const [rows] = await pool.query("SELECT * FROM vehicles");
    res.json(rows);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to fetch vehicles" });
  }
});

/** GET /api/vehicles/:id */
router.get("/:id", async (req, res) => {
  try {
    const [rows] = await pool.query("SELECT * FROM vehicles WHERE id = ?", [
      req.params.id,
    ]);
    if (!rows.length)
      return res.status(404).json({ error: "Vehicle not found" });
    res.json(rows[0]);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to fetch vehicle" });
  }
});

/** POST /api/vehicles */
router.post("/", async (req, res) => {
  try {
    const { plate_number, make, model, year, category, daily_rate, mileage } =
      req.body;
    if (!plate_number || !make || !model || !year) {
      return res.status(400).json({ error: "Missing required fields" });
    }
    const [result] = await pool.query(
      `INSERT INTO vehicles (plate_number, make, model, year, category, daily_rate, mileage) VALUES (?, ?, ?, ?, ?, ?, ?)`,
      [
        plate_number,
        make,
        model,
        year,
        category || "economy",
        daily_rate || 0.0,
        mileage || 0,
      ]
    );
    // const [rows] = await pool.query('SELECT * FROM vehicles WHERE id = ?', [result.insertId]);
    // res.status(201).json(rows[0]);
    res
      .status(201)
      .json({ id: result.insertId, message: "Vehicle created successfully" });
  } catch (err) {
    console.error(err);
    if (err.code === "ER_DUP_ENTRY") {
      return res.status(409).json({ error: "Duplicate plate_number" });
    }
    res.status(500).json({ error: "Failed to create vehicle" });
  }
});

/** PUT /api/vehicles/:id */
router.put("/:id", async (req, res) => {
  try {
    const {
      plate_number,
      make,
      model,
      year,
      category,
      status,
      daily_rate,
      mileage,
    } = req.body;
    const [result] = await pool.query(
      `UPDATE vehicles SET plate_number = ?, make = ?, model = ?, year = ?, category = ?, status = ?, daily_rate = ?, mileage = ? WHERE id = ?`,
      [
        plate_number,
        make,
        model,
        year,
        category,
        status,
        daily_rate,
        mileage,
        req.params.id,
      ]
    );
    if (result.affectedRows === 0) {
      return res.status(404).json({ error: "Vehicle not found" });
    }

    res.json({ message: "Vehicle updated successfully" });
    // if (result.affectedRows === 0) return res.status(404).json({ error: 'Vehicle not found' });
    // const [rows] = await pool.query('SELECT * FROM vehicles WHERE id = ?', [req.params.id]);
    // res.json(rows[0]);
  } catch (err) {
    console.error(err);
    if (err.code === "ER_DUP_ENTRY") {
      return res.status(409).json({ error: "Duplicate plate_number" });
    }
    res.status(500).json({ error: "Failed to update vehicle" });
  }
});

/** DELETE /api/vehicles/:id */
router.delete("/:id", async (req, res) => {
  try {
    const [result] = await pool.query("DELETE FROM vehicles WHERE id = ?", [
      req.params.id,
    ]);
    if (result.affectedRows === 0)
      return res.status(404).json({ error: "Vehicle not found" });
    res.json({ message: "Vehicle deleted" });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to delete vehicle" });
  }
});

module.exports = router;
