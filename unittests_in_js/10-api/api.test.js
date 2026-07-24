const { expect } = require('chai');
const request = require('request');

describe('Index page', function () {

  it('should return status code 200', function (done) {

    request.get('http://localhost:7865/', (error, response) => {

      expect(response.statusCode).to.equal(200);

      done();

    });

  });


  it('should return the correct message', function (done) {

    request.get('http://localhost:7865/', (error, response, body) => {

      expect(body).to.equal('Welcome to the payment system');

      done();

    });

  });

});

describe('Cart page', function () {

  it('should return status code 200 when id is a number', function (done) {

    request.get('http://localhost:7865/cart/12',
      (error, response) => {

        expect(response.statusCode).to.equal(200);

        done();
      });

  });


  it('should return the correct message when id is a number', function (done) {

    request.get('http://localhost:7865/cart/12',
      (error, response, body) => {

        expect(body).to.equal(
          'Payment methods for cart 12'
        );

        done();
      });

  });


  it('should return 404 when id is not a number', function (done) {

    request.get('http://localhost:7865/cart/hello',
      (error, response) => {

        expect(response.statusCode).to.equal(404);

        done();
      });

  });

});

describe('Available payments page', function () {

  it('should return available payment methods', function (done) {

    request.get(
      'http://localhost:7865/available_payments',
      (error, response, body) => {

        expect(response.statusCode).to.equal(200);

        const result = JSON.parse(body);

        expect(result).to.deep.equal({
          payment_methods: {
            credit_cards: true,
            paypal: false
          }
        });

        done();
      }
    );

  });

});

describe('Login page', function () {

  it('should return welcome message', function (done) {

    request.post(
      {
        url: 'http://localhost:7865/login',
        json: {
          userName: 'Betty'
        }
      },
      (error, response, body) => {

        expect(response.statusCode).to.equal(200);

        expect(body).to.equal(
          'Welcome Betty'
        );

        done();
      }
    );

  });

});