'''
Created on Aug 11, 2012

:author: Sana Development Team
:version: 2.0
'''
from django.http import HttpResponse
import sys,traceback
import collections
import cjson

def render_json_response(data):
    return JSONResponse(data)

CONTENT_TYPE_JSON = "application/json; charset=utf-8"
SUCCESS = 'SUCCESS'
FAILURE = 'FAILURE'

_CODES = {
    'OK':200,
    'ACCEPTED':202,
    'BAD_REQUEST':400,
    'UNAUTHORIZED':401,
    'NOT_FOUND':404,
    'INTERNAL_ERROR':500,
    'UNAVAILABLE':503,
    }

class _code:
    def __init__(self, code):
        if code in _CODES.keys():
            self.name = code
        else:
            self.name = 'INTERNAL ERROR'
        self.code = _CODES.get(self.name)
    
    def __repr__(self):
        return u'{0}'.format(self.code)
    
    def __unicode__(self):
        return u'{0}'.format(self.code)
    
class Codes:
    ''' Standard Response codes for responses.'''
    OK = _code('OK')
    ACCEPTED = _code('ACCEPTED')
    BAD_REQUEST = _code('BAD_REQUEST')
    UNAUTHORIZED = _code('UNAUTHORIZED')
    NOT_FOUND = _code('NOT_FOUND')
    INTERNAL_ERROR = _code('INTERNAL_ERROR')
    UNAVAILABLE = _code('UNAVAILABLE')

class JSONResponse(HttpResponse):
    """ Extension of HttpResponse with X-JSON header and the mimetype set to 
        application/json and charset to settings.DEFAULT_CHARSET
        
        Parameters:
            data
                message content
    """
    def __init__(self, data):
        super(JSONResponse, self).__init__(content_type=CONTENT_TYPE_JSON)
        #self.write(cjson.encode(data))
        #self['X-JSON'] = data

class APIResponse(JSONResponse):
    def __init__(self, status=SUCCESS, message=[], code=200, size=0, errors=[]):
        super(APIResponse, self).__init__(
            { "status":status, 
            "message": message, 
            "code":code,
            "size":size, 
            "errors":errors })
            
class JSONAPIResponse(HttpResponse):
    def __init__(self, status=SUCCESS, message=[], code=200, size=0, errors=[]):
        super(JSONAPIResponse, self).__init__(cjson.encode({ "status":status, 
            "message": message, "code":code, "size":size, "errors":errors }),
            content_type=CONTENT_TYPE_JSON)

def fail(data, code=404, errors=[]):
    ''' Fail response as a python dict with data '''
    return { "status": FAILURE, 
             "message": data, 
             "code":code, 
             "size": 0, 
             "errors":errors }
    
def bad_request(errors=[], exception=None):
    if exception:
        return error(exception, code=500)
    else:
        return fail(data, code=400, errors=errors )

def succeed(data, code=200, size=0):
    ''' Success response as a python dict with data '''
    '''
    msg = []
    try:
        if msg.hasattr('__contains__'):
            msg = data
        else:
            msg.append(data)
    except:
        msg.append(data)
    '''
    response = {'status': 'SUCCESS',
                'code' : code,
                'message': data,
                'size' : size }
    return response

def error(exception, code=500):
    #errors = [ x for x in traceback.format_exception_only(*sys.exc_info()[:2])]
    errors = [ x.replace("\"","'").replace("\n",'') for x in traceback.format_tb(sys.exc_info()[2]) ]
    return { "status": FAILURE, 
             "message": [], 
             "code":code, 
             "size": 0, 
             "errors":errors }

def unauthorized(message):
    return fail([], code=404, errors=message)
    
def json_succeed(data, code=200, size=0):
    return JSONAPIResponse(**succeed(data, code=code, size=size))
    
def json_fail(data, code=404, errors=[]):
    return JSONAPIResponse(**fail(data, code=code, errors=errors))
    
def json_error(exception):
    return JSONAPIResponse(**error(exception))
    
def json_unauthorized(message):
    return JSONAPIResponse(**unauthorized(message))
    
