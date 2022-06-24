
# Doc: https://docs.aiogram.dev/en/latest/examples/middleware_and_antiflood.html
def rate_limit(limit: int, key=None):

    def decorator(func):
        setattr(func, 'throlling_rate_limit', limit)
        if key:
            setattr(func, 'throlling_key', key)
        
        return func
    
    return decorator