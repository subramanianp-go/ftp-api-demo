# ftp-api-demo
API that fronts an ftp server

## install dependencies
`pip install -r requirements.txt`

## run the server
`uvicorn ftpApi:app`

## postman collection to test
### List files
`curl --location --request GET 'http://localhost:8000/listFiles'`
### Store file in ftp
Note: ensure the file you send is not already present in the server
`curl --location --request POST 'http://localhost:8000/store' \
--header 'Content-Type: application/json' \
--data-raw '{
    "file": "sales-sample.csv"
}'`
### Retrieve file from ftp
Note: ensure you see your downloaded file in local directory prefixed with 'downloaded-'
`curl --location --request POST 'http://localhost:8000/retrieve' \
--header 'Content-Type: application/json' \
--data-raw '{
    "file": "sales-sample.csv"
}'`
