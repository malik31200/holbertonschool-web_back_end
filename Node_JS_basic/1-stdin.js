process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.on('data', (input) => {
  // process.stdin to read the user input
  const name = input.toString().trim();
  // input is a buffer, convert it to a string and remove the line break.
  process.stdout.write(`Your name is: ${name}\n`);
});
process.stdin.on('end', () => { // ctrl + D
  process.stdout.write('This important software is now closing\n');
});
