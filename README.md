# Simple Server Providing a Web API with Flask
A basic web API built with Flask that handles **GET** and **POST** requests and returns JSON responses.


## Usage
- GET /hello
    ```sh
    curl -X GET http://127.0.0.1:5000/hello
    ```

- POST /process
    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"name": "Alice"}' http://127.0.0.1:5000/process
    ```


## Concept
[Visit (takehika0129.github.io)](https://takehika0129.github.io/takehika-github-pages/reviews/prototype19.html).


## Requirements
- Python 3.x
- `Flask`

Install dependencies:
```sh
pip install -r requirements.txt
```

## License
You are free to use this code for personal and educational purposes. Commercial use and redistribution are not allowed.
