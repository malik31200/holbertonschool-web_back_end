const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', function () {

  describe('SUM', function () {
    it('should add rounded numbers', function () {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it('should round down numbers', function () {
      assert.strictEqual(calculateNumber('SUM', 1.2, 3.2), 4);
    });
  });


  describe('SUBTRACT', function () {
    it('should subtract rounded numbers', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    it('should handle negative results', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 5, 10), -5);
    });
  });


  describe('DIVIDE', function () {
    it('should divide rounded numbers', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('should return Error when dividing by zero', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
  });

});
