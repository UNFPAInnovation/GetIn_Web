from django.conf import settings

class APIKeyAuthenticator(object):
    def process_request(self, request):
        auth = request.META.get("HTTP_AUTHORIZATION", None)
        if auth and auth.startswith('Bearer'):
            authenticated = False
            token = None
            try:
                token_type, token = auth.split(":")
            except:
                pass
            # Check authentication token
            if token and token.strip() == settings.API_KEY_UPDATE:
                authenticated = True
            setattr(request,'authenticated', authenticated)
        return None
