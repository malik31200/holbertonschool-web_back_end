const { expect } = require('chai');
const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function () {
  it('should call Utils.calculateNumber with SUM, 100 and 20', function () {
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);

    const logSpy = sinon.spy(console, 'log');

    sendPaymentRequestToApi(100, 20);

    expect(stub.calledOnceWith('SUM', 100, 20)).to.be.true;

    expect(logSpy.calledOnceWith('The total is: 10')).to.be.true;

    stub.restore();
    logSpy.restore();
  });
});