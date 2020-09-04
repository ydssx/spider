from log_config import logger
import redis


class RedisManager:
    """redis连接设置
    """
    def __init__(self):
        self.logger = logger()

    def init_client(self, host='localhost', port=None, password=None, db=0):
        try:
            pool = redis.ConnectionPool(host=host,
                                        port=port,
                                        db=db,
                                        password=password,
                                        decode_responses=True)
            client = redis.Redis(connection_pool=pool)
            self.logger.debug('hello world')
        except Exception as e:
            self.logger.error("connect redis failed,msg={}".format(e))
            return None
        return client

    def __call__(self):
        return self.init_client()

a=RedisManager()