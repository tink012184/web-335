/*
  Author: Melissa Lutz
  Date: 2025-09-10
  File: Lutz-HandsOn5_1.js
  Description: MongoDB Shell queries for insert, update, and projection on 'users' collection.
*/

use("web335DB");

// (a) INSERT new user and PROOF
// Adds a user matching schema fields and validates insertion
db.users.insertOne({
  firstName: "Ada",
  lastName: "Lovelace",
  email: "ada.lovelace@example.com",
  employeeId: 9999,
  dateCreated: new Date(),
});
db.users.find(
  { email: "ada.lovelace@example.com" },
  { _id: 0, firstName: 1, lastName: 1, email: 1, employeeId: 1 }
);

// (b) UPDATE Mozart email and PROOF
// Updates Mozart's email and validates the change
db.users.updateOne(
  { lastName: "Mozart" },
  { $set: { email: "mozart@me.com" } }
);
db.users.find(
  { lastName: "Mozart" },
  { _id: 0, firstName: 1, lastName: 1, email: 1 }
);

// (c) PROJECTION of all users
// Shows all users with only firstName, lastName, email
db.users.find({}, { _id: 0, firstName: 1, lastName: 1, email: 1 });
