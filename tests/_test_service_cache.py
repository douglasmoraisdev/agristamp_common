import os
import pytest
from agristamp_common.utils.services import cache_or_service_get
from agristamp_common.utils.cache import redis_hset


@pytest.mark.asyncio
async def test_cache():

    key = 'allianz_service'
    field = 'culturas_service/culturas/allianz/feijao'
    value = { "id_agristamp": 8, "id_allianz": 7 }

    await redis_hset(key, field, value)

    cached = await cache_or_service_get(key, field)

    assert cached is not None
    assert cached['id_agristamp'] == 8
    assert cached['id_allianz'] == 7
