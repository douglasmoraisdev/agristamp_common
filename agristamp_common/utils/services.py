import requests
import os

def service_get(service_slug, **query):
   
    service_url = f"{os.getenv('CLUSTER_URL')}/{os.getenv('stage')}/{service_slug}"
    
    request = requests.get(service_url, query)

    return request



def service_post(service_slug, payload):
       
    service_url = f"{os.getenv('CLUSTER_URL')}/{os.getenv('stage')}/{service_slug}"
    
    request = requests.post(service_url, data=payload)

    return request
