API Endpoints
POST /add_to_cart/ - Add a product to the cart   -   http://127.0.0.1:8000/add_to_cart/


GET /view_cart - View the user's cart, including total price -   http://127.0.0.1:8000/view_cart


GET /products/ - List all products - http://127.0.0.1:8000/products


GET /users/ - Get a list of all users - http://127.0.0.1:8000/users/


POST /register/ - Register a new user - http://127.0.0.1:8000/register/


POST /user_login/ - Log in an existing user - http://127.0.0.1:8000/user_login/


1. Register a User:

Endpoint: http://127.0.0.1:8000/register/
Method: POST

{
  "username": "niveditha",
  "email": "niveditha@example.com",
  "password": "123"
}

2. Login a User:

Endpoint: http://127.0.0.1:8000/user_login/
Method: POST

{
  "username": "niveditha",
  "password": "123"
}

3. Add a Product to the Cart:

Endpoint: http://127.0.0.1:8000/add_to_cart/
Method: POST

{
  "product_id": 1,
  "quantity": 2
}

4. View the Cart:

Endpoint: http://127.0.0.1:8000/view_cart
Method: GET

Output
{
  "car_items": [
    {
      "id":1,
      "quantity":2
    }
  ],
  "total_price":20.0
}


5. View Products:

Endpoint: http://127.0.0.1:8000/products/
Method: GET
