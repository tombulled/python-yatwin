from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing login (an instance of <ParamMethod>)

Constants defined here:
    ENDPOINT
    DESCRIPTION
    GET_PARAMETERS
    POST_PARAMETERS
    RETURNS
    METHOD
    FILES

Imports:
    .method_types
    ..parameters
    .constants.permissions
    .constants.methods
"""

ENDPOINT = 'login.cgi'
DESCRIPTION = 'get the IE login latest user name, password and privileges'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
    parameters.PRI,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

login = method_types.ParamMethod \
(
    endpoint = ENDPOINT,
    description = DESCRIPTION,
    get_parameters = GET_PARAMETERS,
    post_parameters = POST_PARAMETERS,
    returns = RETURNS,
    permission = PERMISSION,
    method = METHOD,
    files = FILES,
)
