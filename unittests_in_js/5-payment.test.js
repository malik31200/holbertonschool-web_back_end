const { expect } = require('chai');
const sinon = require('sinon');

const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', function () {
  let logSpy;

  beforeEach(function () {
    logSpy = sinon.spy(console, 'log');
  });

  afterEach(function () {
    logSpy.restore();
  });

  it('should log the correct total for 100 and 20', function () {
    sendPaymentRequestToApi(100, 20);

    expect(logSpy.calledOnce).to.be.true;

    expect(logSpy.calledWith('The total is: 120')).to.be.true;
  });

  it('should log the correct total for 10 and 10', function () {
    sendPaymentRequestToApi(10, 10);

    expect(logSpy.calledOnce).to.be.true;

    expect(logSpy.calledWith('The total is: 20')).to.be.true;
  });
});