import requests
import base64
import urllib
import os
from .cache import redis_set, redis_hget
import json
import boto3
from dotmap import DotMap


def _generate_api_gateway_post(body: dict, path: str, endpoint: str, stage: str, service_slug: str):

    #body = body.encode()

    requestContext_path = f'/{stage}{path}'
    resourcePath =  f'/{service_slug}/'+'{proxy+}'
    #base64_body = base64.b64encode(str(body).encode())

    base64_body = urllib.parse.urlencode(body, doseq=False)

    payload = {
        "body": base64_body,
        "path": path,
        "resource": resourcePath,
        "httpMethod": "POST",
        "isBase64Encoded": False,
        "multiValueQueryStringParameters": {},
        "pathParameters": {
            "proxy": endpoint
        },
        "stageVariables": {
            "alias": stage
        },
        "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "en-US,en;q=0.8",
            "Cache-Control": "max-age=0",
            "CloudFront-Forwarded-Proto": "https",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-Mobile-Viewer": "false",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Is-Tablet-Viewer": "false",
            "CloudFront-Viewer-Country": "US",
            "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Custom User Agent String",
            "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "X-Amz-Cf-Id": "cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
            "X-Forwarded-Port": "443",
            "X-Forwarded-Proto": "https"
        },
        "multiValueHeaders": {
            "Accept": [
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
            ],
            "Accept-Encoding": [
            "gzip, deflate, sdch"
            ],
            "Accept-Language": [
            "en-US,en;q=0.8"
            ],
            "Cache-Control": [
            "max-age=0"
            ],
            "CloudFront-Forwarded-Proto": [
            "https"
            ],
            "CloudFront-Is-Desktop-Viewer": [
            "true"
            ],
            "CloudFront-Is-Mobile-Viewer": [
            "false"
            ],
            "CloudFront-Is-SmartTV-Viewer": [
            "false"
            ],
            "CloudFront-Is-Tablet-Viewer": [
            "false"
            ],
            "CloudFront-Viewer-Country": [
            "US"
            ],
            "Host": [
            "0123456789.execute-api.us-east-1.amazonaws.com"
            ],
            "Upgrade-Insecure-Requests": [
            "1"
            ],
            "User-Agent": [
            "Custom User Agent String"
            ],
            "Via": [
            "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)"
            ],
            "X-Amz-Cf-Id": [
            "cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA=="
            ],
            "X-Forwarded-For": [
            "127.0.0.1, 127.0.0.2"
            ],
            "X-Forwarded-Port": [
            "443"
            ],
            "X-Forwarded-Proto": [
            "https"
            ]
        },
        "requestContext": {
                "accountId": "123456789012",
                "resourceId": "123456",
                "stage": "prod",
                "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
                "requestTime": "09/Apr/2015:12:34:56 +0000",
                "requestTimeEpoch": 1428582896000,
                "identity": {
                "cognitoIdentityPoolId": None,
                "accountId": None,
                "cognitoIdentityId": None,
                "caller": None,
                "accessKey": None,
                "sourceIp": "127.0.0.1",
                "cognitoAuthenticationType": None,
                "cognitoAuthenticationProvider": None,
                "userArn": None,
                "userAgent": "Custom User Agent String",
                "user": None
            },
            "path": requestContext_path,            
            "resourcePath": resourcePath,
            "stage": stage,
            "httpMethod": "POST",
            "apiId": "1234567890",
            "protocol": "HTTP/1.1"
        }
    }

    return payload


def _generate_api_gateway_get(query: dict, path: str, endpoint: str, stage: str, service_slug: str):

    requestContext_path = f'/{stage}{path}'
    resourcePath =  f'/{service_slug}/'+'{proxy+}'

    payload = {
            "resource": resourcePath,
            "path": path,
            "httpMethod": "GET",
            "multiValueQueryStringParameters": query,
            "pathParameters": {
                "proxy": endpoint
            },
            "stageVariables": {
                "alias": stage
            },
            "headers": {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, sdch",
                "Accept-Language": "en-US,en;q=0.8",
                "Cache-Control": "max-age=0",
                "CloudFront-Forwarded-Proto": "https",
                "CloudFront-Is-Desktop-Viewer": "true",
                "CloudFront-Is-Mobile-Viewer": "false",
                "CloudFront-Is-SmartTV-Viewer": "false",
                "CloudFront-Is-Tablet-Viewer": "false",
                "CloudFront-Viewer-Country": "US",
                "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Custom User Agent String",
                "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
                "X-Amz-Cf-Id": "cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA==",
                "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
                "X-Forwarded-Port": "443",
                "X-Forwarded-Proto": "https"
            },
            "multiValueHeaders": {
                "Accept": [
                    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
                ],
                "Accept-Encoding": [
                    "gzip, deflate, sdch"
                ],
                "Accept-Language": [
                    "en-US,en;q=0.8"
                ],
                "Cache-Control": [
                    "max-age=0"
                ],
                "CloudFront-Forwarded-Proto": [
                    "https"
                ],
                "CloudFront-Is-Desktop-Viewer": [
                    "true"
                ],
                "CloudFront-Is-Mobile-Viewer": [
                    "false"
                ],
                "CloudFront-Is-SmartTV-Viewer": [
                    "false"
                ],
                "CloudFront-Is-Tablet-Viewer": [
                    "false"
                ],
                "CloudFront-Viewer-Country": [
                    "US"
                ],
                "Host": [
                    "0123456789.execute-api.us-east-1.amazonaws.com"
                ],
                "Upgrade-Insecure-Requests": [
                    "1"
                ],
                "User-Agent": [
                    "Custom User Agent String"
                ],
                "Via": [
                    "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)"
                ],
                "X-Amz-Cf-Id": [
                    "cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA=="
                ],
                "X-Forwarded-For": [
                    "127.0.0.1, 127.0.0.2"
                ],
                "X-Forwarded-Port": [
                    "443"
                ],
                "X-Forwarded-Proto": [
                    "https"
                ]
            },
            "requestContext": {
                "accountId": "123456789012",
                "resourceId": "123456",
                "stage": "prod",
                "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
                "requestTime": "09/Apr/2015:12:34:56 +0000",
                "requestTimeEpoch": 1428582896000,
                "identity": {
                    "cognitoIdentityPoolId": None,
                    "accountId": None,
                    "cognitoIdentityId": None,
                    "caller": None,
                    "accessKey": None,
                    "sourceIp": "127.0.0.1",
                    "cognitoAuthenticationType": None,
                    "cognitoAuthenticationProvider": None,
                    "userArn": None,
                    "userAgent": "Custom User Agent String",
                    "user": None
                },
                "path": requestContext_path,
                "resourcePath": resourcePath,
                "stage": stage,
                "httpMethod": "GET",
                "apiId": "1234567890",
                "protocol": "HTTP/1.1"
            }
        }

    return payload


def lambda_get(service_slug: str, endpoint: str, query: dict):

    client = boto3.client('lambda')

    # retira a barra do endpoint
    if endpoint[0] == '/':
        endpoint = endpoint[1:]

    stage = os.getenv('STAGE')
    path = f"/{service_slug}/{endpoint}"
    function_name = f"{service_slug}_function"

    payload = _generate_api_gateway_get(query=query, path=path, endpoint=endpoint, stage=stage, service_slug=service_slug)

    response = client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse',
        LogType='Tail',
        ClientContext=base64.b64encode(b'{"custom":{"foo":"bar", "fuzzy":"wuzzy"}}').decode('utf-8'),
        Payload=json.dumps(payload),
        Qualifier=stage
    )

    raw_payload = response['Payload'].read()
    try:
        response_payload = json.loads(raw_payload)
        response_body = json.loads(response_payload['body'])

    except json.decoder.JSONDecodeError:
        response_body = raw_payload

    json_attr = lambda :response_body

    response_obj = DotMap()
    response_obj.status_code = response_payload['statusCode']
    response_obj.headers = response['ResponseMetadata']['HTTPHeaders']
    response_obj.text = raw_payload
    response_obj.json = json_attr
    response_obj.error = response['FunctionError'] if 'FunctionError' in response else None

    return response_obj


def lambda_post(service_slug: str, endpoint: str, body: dict):

    client = boto3.client('lambda')

    # retira a barra do endpoint
    if endpoint[0] == '/':
        endpoint = endpoint[1:]

    stage = os.getenv('STAGE')
    path = f"/{service_slug}/{endpoint}"
    function_name = f"{service_slug}_function"

    payload = _generate_api_gateway_post(body=body, path=path, endpoint=endpoint, stage=stage, service_slug=service_slug)

    response = client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse',
        LogType='Tail',
        ClientContext=base64.b64encode(b'{"custom":{"foo":"bar", "fuzzy":"wuzzy"}}').decode('utf-8'),
        Payload=json.dumps(payload),
        Qualifier=stage
    )

    raw_payload = response['Payload'].read()
    try:
        response_payload = json.loads(raw_payload)
        response_body = json.loads(response_payload['body'])

    except json.decoder.JSONDecodeError:
        response_body = raw_payload

    json_attr = lambda :response_body

    response_obj = DotMap()
    response_obj.status_code = response_payload['statusCode']
    response_obj.headers = response['ResponseMetadata']['HTTPHeaders']
    response_obj.text = raw_payload
    response_obj.json = json_attr
    response_obj.error = response['FunctionError'] if 'FunctionError' in response else None

    return response_obj


def service_get(service_slug, endpoint, headers=None, query=None, force_api_gateway=False):


    if (os.getenv('USE_LAMBDA_SDK', False) == '1') and (not force_api_gateway):

        print('service_get -> SDK LAMBDA')
        return lambda_get(service_slug, endpoint, query)

    else:

        print('service_get -> API GATEWAY')

        # retira a barra do endpoint
        if endpoint[0] == '/':
            endpoint = endpoint[1:]

        service_url = f"{os.getenv('CLUSTER_URL')}/{os.getenv('STAGE')}/{service_slug}/{endpoint}"

        request = requests.get(service_url, params=query, headers=headers)

        return request


def service_post(service_slug, endpoint, headers=None, payload=None, force_api_gateway=False):

    if (os.getenv('USE_LAMBDA_SDK', False) == '1') and (not force_api_gateway):

        print('service_get -> SDK LAMBDA')
        return lambda_post(service_slug, endpoint, payload)

    else:

        print('service_get -> API GATEWAY')
        # retira a barra do endpoint
        if endpoint[0] == '/':
            endpoint = endpoint[1:]

        service_url = f"{os.getenv('CLUSTER_URL')}/{os.getenv('STAGE')}/{service_slug}/{endpoint}"

        request = requests.post(service_url, data=payload, headers=headers)

        return request


async def cache_or_service_get(service_slug, endpoint, headers=None, query=None, use_cache=True):

    is_cached = False

    if use_cache:

        cached = await redis_hget(service_slug, endpoint)

        if cached:
            is_cached = True
            request = cached

        else:
            request = service_get(service_slug, endpoint, headers, query)

    else:
        request = service_get(service_slug, endpoint, headers, query)

    return is_cached, request
