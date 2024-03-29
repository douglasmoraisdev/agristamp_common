import requests
import base64
import urllib
import os
from .cache import redis_set, redis_hget
import json
import boto3
from dotmap import DotMap

from agristamp_common.utils.logs import logger

def _generate_api_gateway_post(body: dict, path: str, endpoint: str, stage: str, service_slug: str, cookies: dict):

    #body = body.encode()

    requestContext_path = f'/{stage}{path}'
    resourcePath =  f'/{service_slug}/'+'{proxy+}'
    #base64_body = base64.b64encode(str(body).encode())

    base64_body = urllib.parse.urlencode(body, doseq=False)
    if cookies:
        send_cookies = urllib.parse.urlencode(cookies, doseq=False)
    else:
        send_cookies = ''

    payload = {
        "body": base64_body,
        "headers": {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "CloudFront-Forwarded-Proto": "https",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-Mobile-Viewer": "false",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Is-Tablet-Viewer": "false",
            "CloudFront-Viewer-Country": "US",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": send_cookies,
            "Host": "j8mj59343f.execute-api.us-east-1.amazonaws.com",
            "User-Agent": "python-requests/2.25.1",
            "Via": "1.1 f9efe5e72b7e5cc47bf34a0b0debcbe2.cloudfront.net (CloudFront)",
            "X-Amz-Cf-Id": "-qHuqC-YS36C7cnoHqsam9fkGdOoR86LGndRRsczPWQ6AfIUEM4_ag==",
            "X-Amzn-Trace-Id": "Root=1-60f6eeaf-458ccae85084fb5670584faa",
            "X-Forwarded-For": "18.209.99.174, 70.132.33.145",
            "X-Forwarded-Port": "443",
            "X-Forwarded-Proto": "https"
        },
        "httpMethod": "POST",
        "isBase64Encoded": False,
        "multiValueHeaders": {
            "Accept": [
                "*/*"
            ],
            "Accept-Encoding": [
                "gzip, deflate"
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
            "Content-Type": [
                "application/x-www-form-urlencoded"
            ],
            "Cookie": [
                send_cookies
            ],
            "Host": [
                "j8mj59343f.execute-api.us-east-1.amazonaws.com"
            ],
            "User-Agent": [
                "python-requests/2.25.1"
            ],
            "Via": [
                "1.1 f9efe5e72b7e5cc47bf34a0b0debcbe2.cloudfront.net (CloudFront)"
            ],
            "X-Amz-Cf-Id": [
                "-qHuqC-YS36C7cnoHqsam9fkGdOoR86LGndRRsczPWQ6AfIUEM4_ag=="
            ],
            "X-Amzn-Trace-Id": [
                "Root=1-60f6eeaf-458ccae85084fb5670584faa"
            ],
            "X-Forwarded-For": [
                "18.209.99.174, 70.132.33.145"
            ],
            "X-Forwarded-Port": [
                "443"
            ],
            "X-Forwarded-Proto": [
                "https"
            ]
        },
        "multiValueQueryStringParameters": None,
        "path": path,
        "pathParameters": {
            "proxy": endpoint
        },
        "queryStringParameters": None,
        "requestContext": {
            "accountId": "521871819478",
            "apiId": "j8mj59343f",
            "domainName": "j8mj59343f.execute-api.us-east-1.amazonaws.com",
            "domainPrefix": "j8mj59343f",
            "extendedRequestId": "Cxo7aHrrIAMFTtQ=",
            "httpMethod": "POST",
            "identity": {
                "accessKey": None,
                "accountId": None,
                "caller": None,
                "cognitoAuthenticationProvider": None,
                "cognitoAuthenticationType": None,
                "cognitoIdentityId": None,
                "cognitoIdentityPoolId": None,
                "principalOrgId": None,
                "sourceIp": "18.209.99.174",
                "user": None,
                "userAgent": "python-requests/2.25.1",
                "userArn": None
            },
            "path": requestContext_path,
            "protocol": "HTTP/1.1",
            "requestId": "760ce857-da0b-4699-8194-d57bce7cc549",
            "requestTime": "20/Jul/2021:15:41:35 +0000",
            "requestTimeEpoch": 1626795695299,
            "resourceId": "6dlorr",
            "resourcePath": resourcePath,
            "stage": stage
        },
        "resource": resourcePath,
        "stageVariables": {
            "lambdaAlias": stage
        }
    }

    return payload


def _generate_api_gateway_get(query: dict, path: str, endpoint: str, stage: str, service_slug: str, cookies: dict):

    requestContext_path = f'/{stage}{path}'
    resourcePath =  f'/{service_slug}/'+'{proxy+}'
    if cookies:
        send_cookies = urllib.parse.urlencode(cookies, doseq=False)
    else:
        send_cookies = ''

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
                "Cookie": send_cookies,
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
                "Cookie": [
                    send_cookies
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


def lambda_get(service_slug: str, endpoint: str, query: dict, cookies: dict = None):

    client = boto3.client('lambda')

    # retira a barra do endpoint
    if endpoint[0] == '/':
        endpoint = endpoint[1:]

    stage = os.getenv('STAGE')
    path = f"/{service_slug}/{endpoint}"
    function_name = f"{service_slug}_function"

    payload = _generate_api_gateway_get(query=query, path=path, endpoint=endpoint, stage=stage, service_slug=service_slug, cookies=cookies)

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


def lambda_post(service_slug: str, endpoint: str, body: dict, cookies: dict = None):

    client = boto3.client('lambda')

    # retira a barra do endpoint
    if endpoint[0] == '/':
        endpoint = endpoint[1:]

    stage = os.getenv('STAGE')
    path = f"/{service_slug}/{endpoint}"
    function_name = f"{service_slug}_function"

    payload = _generate_api_gateway_post(body=body, path=path, endpoint=endpoint, stage=stage, service_slug=service_slug, cookies=cookies)

    logger.info(f'Enviando POST via LAMBDA para {service_slug} data:[{payload}]')
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

    logger.info(f'Resultado do POST via LAMBDA para {service_slug}: {response_obj.status_code}')

    return response_obj


def service_get(service_slug, endpoint, headers=None, query=None, force_api_gateway=False, cookies=None, hash_proposta=''):


    if (os.getenv('USE_LAMBDA_SDK', False) == '1') and (not force_api_gateway):

        print('service_get -> SDK LAMBDA')
        return lambda_get(service_slug, endpoint, query, cookies)

    else:

        print('service_get -> API GATEWAY')

        # retira a barra do endpoint
        if endpoint[0] == '/':
            endpoint = endpoint[1:]

        service_url = f"{os.getenv('CLUSTER_URL')}/{os.getenv('STAGE')}/{service_slug}/{endpoint}"
        if hash_proposta != '' and hash_proposta is not None:
            headers.update({'Hash': hash_proposta})

        logger.info(f'Enviando GET {service_url} headers:[{headers}] cookies: [{cookies}]',
                      extra={'hash_proposta': hash_proposta, 'data': query})
        request = requests.get(service_url, params=query, headers=headers, cookies=cookies)

        if request.status_code == 200:
            logger.info(f'Resultado do GET para {service_url}: {request.status_code}', extra={'hash_proposta': hash_proposta, 'data': request.json()})
        else:
            logger.info(f'Resultado do GET para {service_url}: {request.status_code}', extra={'hash_proposta': hash_proposta, 'data': request.text})

        return request


def service_post(service_slug, endpoint, headers=None, payload=None, force_api_gateway=False, cookies=None, hash_proposta=''):

    if (os.getenv('USE_LAMBDA_SDK', False) == '1') and (not force_api_gateway):

        print('service_get -> SDK LAMBDA')
        return lambda_post(service_slug, endpoint, payload)

    else:

        print('service_get -> API GATEWAY')
        # retira a barra do endpoint
        if endpoint[0] == '/':
            endpoint = endpoint[1:]

        service_url = f"{os.getenv('CLUSTER_URL')}/{os.getenv('STAGE')}/{service_slug}/{endpoint}"
        if hash_proposta != '' and hash_proposta is not None:
            headers.update({'Hash': hash_proposta})

        logger.info(f'Enviando POST {service_url} headers:[{headers}] cookies: [{cookies}]',
                      extra={'hash_proposta': hash_proposta, 'data': payload})
        request = requests.post(service_url, data=payload, headers=headers, cookies=cookies)
        if request.status_code == 200:
            logger.info(f'Resultado do POST para {service_url}: {request.status_code}', extra={'hash_proposta': hash_proposta, 'data': request.json()})
        else:
            logger.info(f'Resultado do POST para {service_url}: {request.status_code}', extra={'hash_proposta': hash_proposta, 'data': request.text})

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
