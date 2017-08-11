"""A simple wrapper for the DevRant public HTTP API"""

import urllib.request
import urllib.parse
from enum import Enum
import json

__version__ = '0.1.0'
base_url = 'https://devrant.io/api/'

class SortType:
    """Sort types user for sorting rants"""
    ALGO = 'algo'
    RECENT = 'recent'
    TOP = 'top'

def get_rants(sorting = SortType.ALGO, limit = 20, skip = 0):
    """
    Get rants according to provided parameters

    Args:
        sorting: The sorting type used; either 'algo', 'recent' or 'top'. (Use SortType class for convenience)
        limit: The maximum number of rants to be fetched.
        skip: How many rants to skip from the top of the sort result.

    Returns:
        A list of rants
    """
    params = {}
    params['sort'] = sorting
    params['limit'] = limit
    params['skip'] = skip

    return get_request('devrant/rants', params)['rants']

def get_rant(rant_id):
    """
    Get the rant with specified id.

    Args:
        rant_id: The id of the rant.

    Returns:
        A rant object for the specified ID.
    """
    return get_request('devrant/rants/' + str(rant_id))

def search_rants(term):
    """
    Search for rants containing the given term.
    The term can be contained both in the rant itself, in username, and in tags.

    Args:
        term: The term to be searched for.

    Returns:
        A list of rants resulting from the search.
    """
    params = {'term': term}

    return get_request('devrant/search', params)

def get_user(user_id):
    """
    Get the user with the given ID.

    Args:
        user_id: The ID of the user

    Returns:
        The user corresponding to the given ID.
    """
    return get_request('users/' + str(user_id))

def get_id_from_username(username):
    """
    Get the ID belonging to the user with given username.

    Args:
        username: The username of the user.abs

    Returns:
        The ID of the user with the given username.
    """
    params = {'username': username}

    return get_request('get-user-id', params)['user_id']

def get_request(url, params = None):
    """
    Sends a request to given url with given parameters. Only meant for internal use.
    """
    if not params:
        params = {}

    params['app'] = 3
    full_url = base_url + url + '?' + urllib.parse.urlencode(params)

    return json.loads(urllib.request.urlopen(full_url).read())
