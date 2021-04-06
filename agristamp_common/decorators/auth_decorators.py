import os
from functools import wraps
from fastapi import HTTPException

from agristamp_common.utils.services import service_get


#decorator
def auth_required_fastapi(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        auth_header = kwargs['Authorization']

        if auth_header[:6] == 'Bearer':
            token = auth_header[7:]

        else:
            raise HTTPException(500, 'Invalid Authorization header')
        
        # Try authenticate
        auth_service_slug = 'auth_service'
        auth_endpoint = f'auth/users/services/{os.getenv("SERVICE_SLUG")}'
        auth_header = {'Authorization': f'Bearer {token}'}

        auth_status = service_get(auth_service_slug, auth_endpoint, auth_header)
        if auth_status.status_code == 200:
            kwargs['current_user'] = auth_status.json()
            return await func(*args, **kwargs)
        else:
            raise HTTPException(auth_status.status_code, auth_status.json()['errors'])

    return wrapper
