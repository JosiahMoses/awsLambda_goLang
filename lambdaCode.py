import urllib.request
import json
print("Loading function")

def lambda_handler(event, context):
    #1. Parse out query string params
    ipAddress = event['queryStringParameters']['ipAddress']
    
    print('ipAddress=' + ipAddress)
    
    #2. Construct the body of the respose object
    ipAddressResponse = {}
    ipAddressResponse['ipAddress'] = ipAddress
    ipAddressResponse['message'] = 'Hello from Lambda'
    
    #3. Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(ipAddressResponse)
    
    return responseObject