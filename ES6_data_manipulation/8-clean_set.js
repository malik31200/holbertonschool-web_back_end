export default function cleanSet(set, starString) {
  if (!starString || typeof starString !== 'string') {
    return '';
  }
  const result = [];
  for (const value of set) {
    if (typeof value === 'string' && value.startsWith(starString)) {
      const rest = value.slice(starString.length);
      if (rest) {
        result.push(rest);
      }
    }
  }
  return result.join('-');
}
