function getCurrentYear() {
  return new Date().getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const currentYear = getCurrentYear();

  return {
    [`income-${currentYear}`]: income,
    [`gdp-${currentYear}`]: gdp,
    [`capita-${currentYear}`]: capita,
  };
}
