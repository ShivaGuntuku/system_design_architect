#### API Design

* Create Architecture
    - POST /api/v1/architectures
    - Request: 
        {
            "name": "URL Shortner",
            "desctiption" : "system design practice"
        }
    - Response:
        {
            "id": "UUID",
            "name": "URL Shortner"
        }
* Get Architecture
    - GET /api/v1/architectures/{id}
    