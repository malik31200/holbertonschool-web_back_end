export default function cleanSet(set, starString) {
  if (!starString || starString === 0) {
    return '';
  }
  const result = [];
  for (const value of set) {
    if (value.startsWith(starString)) {
      const rest = value.slice(starString.length);
      if (rest) {
        result.push(rest);
      }
    }
  }
  return result.join('-');
}
