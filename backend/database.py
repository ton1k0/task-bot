from os import getenv
from redis_om import get_redis_connection


redis_db = get_redis_connection(
    host = 'redis-16949.c300.eu-central-1-1.ec2.cloud.redislabs.com',
    port = 16949,
    password = 'Pesm2ERxzIOHyjrmyrEdCxtW45u6Lnc1',
    decode_responses=True
)
