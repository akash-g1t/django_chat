Custom Authentication Middleware for consumers:-


from channels.middleware import BaseMiddleware

class TokenAuthMiddleware(BaseMiddleware):

    async def __call__(self, scope, receive, send):
        scope['user'] = await get_user(scope)
        return await super().__call__(scope, receive, send)
