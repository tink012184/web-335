// Author: Melissa Lutz
// Date: 2025-09-02
// File: Lutz-handsOn4.2.js
// Description: Queries for Hands-On 4.2 - MongoDB Database Setup and Querying

// a. Display all users
db.users.find({});

// b. Display the user with the email address jbach@me.com
db.users.find({ email: "jbach@me.com" });

// c. Display the user with the last name Mozart
db.users.find({ lastName: "Mozart" });

// d. Display the user with the first name Richard
db.users.find({ firstName: "Richard" });

// e. Display the user with employeeId 1010
db.users.find({ employeeId: "1010" });
