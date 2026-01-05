console.log('Welcome to Holberton School, what is your name?');
process.stdin.on('data', (input) => {
  // process.stdin to read the user input
  const name = input.toString().trim();
  // input is a buffer, convert it to a string and remove the line break.
  console.log(`Your name is: ${name}`);
});
process.stdin.on('end', () => { // ctrl + D
  console.log('This important software is now closing');
});
