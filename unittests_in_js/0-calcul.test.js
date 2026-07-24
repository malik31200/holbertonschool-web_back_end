const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function () {

  it('should add two integers', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should round the second number', function () {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should round both numbers', function () {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should round .5 upward', function () {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

});