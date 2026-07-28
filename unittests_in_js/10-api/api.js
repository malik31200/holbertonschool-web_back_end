const express = require('express');

const app = express();

app.use(express.json());

const port = 7865;

app.get('/', (req, res) => {
  res.send('Welcome to the payment system')
});

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

app.get('/cart/:id(\\d+)', (req, res) => {
  res.send(`Payment methods for cart ${req.params.id}`);
});

app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  });
});

app.post('/login', (req, res) => {
  const username = req.body.userName;

  res.send(`Welcome ${username}`);
});

module.exports = app;