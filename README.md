#Review Crawler

##Installation

- pip install -r requirements.txt

##Usage

###Book reviews
- **Run** python main.py

- **Url** http://localhost:5000/api/books?name="book_name"

###Example

-
```
curl -i http://localhost:5000/api/books?name="habbit+of+winning"
```
-
```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 53
Server: Werkzeug/0.14.1 Python/2.7.15
Date: Wed, 05 Dec 2018 17:52:34 GMT

{
  "name": "habbit of winning", 
  "rating": 4.17
}
```
