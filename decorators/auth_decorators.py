from functools import wraps
from fastapi import HTTPException

from utils.services import service_get


#decorator
def auth_required_fastapi(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        settings = kwargs['settings']
        auth_header = kwargs['Authorization']

        if auth_header[:6] == 'Bearer':
            token = auth_header[7:]
        else:
            raise HTTPException(500, 'Invalid Authorization header')
        
        if settings.auth_service_url:

            # Try authenticate
            auth_status = service_get('auth_service', token)
            if auth_status.status_code == 200:
                return await func(*args, **kwargs)

    return wrapper
