const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', function () {

  describe('SUM', function () {
    it('should add rounded numbers', function () {
      expect(
        calculateNumber('SUM', 1.4, 4.5)
      ).to.equal(6);
    });

    it('should round down numbers', function () {
      expect(
        calculateNumber('SUM', 1.2, 3.2)
    ).to.equal(4);
    });
  });


  describe('SUBTRACT', function () {
    it('should subtract rounded numbers', function () {
      expect(
        calculateNumber('SUBTRACT', 1.4, 4.5)
    ).to.equal(-4);
    });

    it('should handle negative results', function () {
      expect(
        calculateNumber('SUBTRACT', 5, 10)
    ).to.equal(-5);
    });
  });


  describe('DIVIDE', function () {
    it('should divide rounded numbers', function () {
      expect(
        calculateNumber('DIVIDE', 1.4, 4.5)
    ).to.equal(0.2);
    });

    it('should return Error when dividing by zero', function () {
      expect(
        calculateNumber('DIVIDE', 1.4, 0)
    ).to.equal('Error');
    });
  });

});