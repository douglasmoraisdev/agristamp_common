import os
from fastapi import Header, HTTPException, Depends
from starlette.status import HTTP_400_BAD_REQUEST
from agristamp_common.utils.services import service_get
from fastapi.security import OAuth2PasswordBearer

from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=os.getenv("AUTH_URL"))


async def auth_required(
    Authorization: str = Header(default=None),
    oauth2_scheme = Depends(oauth2_scheme)
):
    if not Authorization:
        raise HTTPException(HTTP_400_BAD_REQUEST, detail='Invalid Authorization header')
    else:


        # Try authenticate internal client
        if os.getenv("AGRISTAMP_KEY") is not None:
            if Authorization == 'Bearer '+os.getenv("AGRISTAMP_KEY"):
                return {'status': 'ok', 'source': 'agristamp_key'}

        # Try authenticate external client
        auth_service_slug = 'auth_service'
        auth_endpoint = f'auth/users/services/{os.getenv("SERVICE_SLUG")}'
        auth_header = {'Authorization': Authorization}

        auth_status = service_get(auth_service_slug, auth_endpoint, auth_header)
        if auth_status.status_code == 200:
            return auth_status.json()
        elif auth_status.status_code in [502, 404]:
            raise HTTPException(auth_status.status_code, 'Serviço de autenticação indisponível')
        else:
            raise HTTPException(auth_status.status_code, auth_status.json()['errors'])


async def token_required(
    Authorization: str = Header(default=None),
):

    if not Authorization:
        raise HTTPException(HTTP_400_BAD_REQUEST, detail='Invalid Authorization header')

    else:

        # Try authenticate
        authorized_tokens = os.getenv('AUTHORIZED_TOKENS', '').split(',')

        if authorized_tokens is not None:

            for token in authorized_tokens:
                print(token)

                if Authorization == f'Bearer {token}':
                    return {'status': 'ok', 'source': 'agristamp_key'}

            # No token found
            raise HTTPException(HTTP_400_BAD_REQUEST, detail='Invalid Token')


def validate_auth_client(auth_token, seguradora_slug):

    # example seguradora-slug:3930293J2093J2093J2093J
    seguradora_token = auth_token.replace('Bearer ', '').split(':')

    if seguradora_slug == seguradora_token[0]:
        return True
    else:
        raise HTTPException(403, 'Não autorizado')
