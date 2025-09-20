/**************************************************************
 * Name: Melissa Lutz
 * Date: 2025-09-19
 * Assignment: Hands-On 6.1 - Aggregate Queries
 * Course: WEB-335
/* ----------------------------------------------------------
 * (a) Display all students.
 *     Shows every document in the students collection.
 * ---------------------------------------------------------- */
// Command:
db.students.find({}).pretty();

/* ----------------------------------------------------------
 * (b) Add a new student and prove it was added.
 *     IMPORTANT: Match existing schema fields: firstName, lastName,
 *     studentId, houseId.
 * ---------------------------------------------------------- */
// Insert:
db.students.insertOne({
  firstName: "Hermione",
  lastName: "Granger",
  studentId: "s2001",
  houseId: "h1007", // Gryffindor
});
// Prove it was added (by studentId):
db.students.find({ studentId: "s2001" }).pretty();

/* ----------------------------------------------------------
 * (c) Update one property of the student added in (b) and prove it.
 *     Here we update lastName.
 * ---------------------------------------------------------- */
// Update:
db.students.updateOne(
  { studentId: "s2001" },
  { $set: { lastName: "Granger-Weasley" } }
);
// Prove the update:
db.students.find({ studentId: "s2001" }).pretty();

/* ----------------------------------------------------------
 * (d) Delete the student created in (b) and prove removal.
 * ---------------------------------------------------------- */
// Delete:
db.students.deleteOne({ studentId: "s2001" });
// Prove deletion (should return no docs):
db.students.find({ studentId: "s2001" });

/* ----------------------------------------------------------
 * (e) Display all students by house.
 *     ORDER: Houses, then Students
 *     Uses $lookup to join houses -> students by houseId.
 * ---------------------------------------------------------- */
db.houses
  .aggregate([
    {
      $lookup: {
        from: "students",
        localField: "houseId",
        foreignField: "houseId",
        as: "Students",
      },
    },
    {
      $project: {
        _id: 0,
        HouseId: "$houseId",
        Founder: "$founder",
        Mascot: "$mascot",
        Students: {
          $map: {
            input: "$Students",
            as: "s",
            in: {
              firstName: "$$s.firstName",
              lastName: "$$s.lastName",
              studentId: "$$s.studentId",
            },
          },
        },
      },
    },
    { $sort: { HouseId: 1 } },
  ])
  .pretty();

/* ----------------------------------------------------------
 * (f) Display all students in house Gryffindor.
 *     ORDER: Gryffindor, then Students
 *     Gryffindor in the seed data has founder "Godric Gryffindor"
 *     and houseId "h1007". We'll match by founder for readability.
 * ---------------------------------------------------------- */
db.houses
  .aggregate([
    { $match: { founder: "Godric Gryffindor" } },
    {
      $lookup: {
        from: "students",
        localField: "houseId",
        foreignField: "houseId",
        as: "Students",
      },
    },
    {
      $project: {
        _id: 0,
        House: { $literal: "Gryffindor" },
        HouseId: "$houseId",
        Mascot: "$mascot",
        Students: {
          $map: {
            input: "$Students",
            as: "s",
            in: {
              firstName: "$$s.firstName",
              lastName: "$$s.lastName",
              studentId: "$$s.studentId",
            },
          },
        },
      },
    },
  ])
  .pretty();

/* ----------------------------------------------------------
 * (g) Display all students in the house with an Eagle mascot.
 *     ORDER: House, then Students
 *     In the seed data, mascot "Eagle" corresponds to Ravenclaw (houseId "h1009").
 * ---------------------------------------------------------- */
db.houses
  .aggregate([
    { $match: { mascot: "Eagle" } },
    {
      $lookup: {
        from: "students",
        localField: "houseId",
        foreignField: "houseId",
        as: "Students",
      },
    },
    {
      $project: {
        _id: 0,
        House: { $literal: "Ravenclaw" },
        HouseId: "$houseId",
        Mascot: "$mascot",
        Students: {
          $map: {
            input: "$Students",
            as: "s",
            in: {
              firstName: "$$s.firstName",
              lastName: "$$s.lastName",
              studentId: "$$s.studentId",
            },
          },
        },
      },
    },
  ])
  .pretty();
