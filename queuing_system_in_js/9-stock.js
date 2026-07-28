import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);


const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4,
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10,
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2,
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5,
  },
];


function getItemById(id) {
  return listProducts.find(
    (item) => item.id === id
  );
}


function reserveStockById(itemId, stock) {
  return setAsync(`item.${itemId}`, stock);
}


async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);

  if (!stock) {
    return 0;
  }

  return parseInt(stock);
}


// Route product list
app.get('/list_products', (req, res) => {
  const products = listProducts.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  }));

  res.json(products);
});


// Route product detail
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);

  const product = getItemById(itemId);

  if (!product) {
    return res.json({
      status: 'Product not found',
    });
  }

  const reserved = await getCurrentReservedStockById(itemId);

  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity: product.stock - reserved,
  });
});


// Route reservation
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);

  const product = getItemById(itemId);

  if (!product) {
    return res.json({
      status: 'Product not found',
    });
  }


  const reserved = await getCurrentReservedStockById(itemId);

  const available = product.stock - reserved;


  if (available <= 0) {
    return res.json({
      status: 'Not enough stock available',
      itemId,
    });
  }


  await reserveStockById(
    itemId,
    reserved + 1
  );


  return res.json({
    status: 'Reservation confirmed',
    itemId,
  });
});


app.listen(1245, () => {
  console.log('Server listening on port 1245');
});