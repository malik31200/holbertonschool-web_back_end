const assert = require('assert');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function () {

  it('should resolve the payment token', function (done) {

    getPaymentTokenFromAPI(true)
      .then((response) => {

        assert.deepStrictEqual(response, {
            data: 'Successful response from the API'
        });

        done();

      });
  });
});