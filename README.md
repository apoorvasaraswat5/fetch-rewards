# fetch-rewards
This is the implementation of the assesment - https://github.com/fetch-rewards/receipt-processor-challenge

## Commands to run the code

### Docker Build
```docker build -t fetch_flask .```

### Docker Run
```docker run -dp 127.0.0.1:6000:6000 fetch_flask```

## Testing implementation

- POST request on http://127.0.0.1:6000/receipts with example json
- GET request on http://127.0.0.1:6000/{uuid}/points with the generated unique id in {uuid}
