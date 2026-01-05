const fs = require('fs'); // Import the file system module to read files

function countStudents(path) {
  let data = ''; // store file contents

  // read the file synchro
  try {
    data = fs.readFileSync(path, 'utf8');
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const lines = data.split('\n').filter((line) => line.trim() !== '');// ignore empty lines
  const students = lines.slice(1); // ignore the header.

  console.log(`Number of students: ${students.length}`);

  const fields = {}; // Creating an object to store students by field
  students.forEach((line) => {
    const [firstname, , , field] = line.split(','); // retrieve the firstname name and field
    if (!fields[field]) fields[field] = []; // If the field does not exist, create an array
    fields[field].push(firstname); // add the firstname at this field
  });

   Object.keys(fields).forEach((field) =>    {
    console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
  });
}

module.exports = countStudents;
