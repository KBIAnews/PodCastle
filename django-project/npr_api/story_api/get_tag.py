"""
Get tag via NPR Story API.
"""

from django.conf import settings
from .story_api_get import get_dict_from_story_api

public_org_id = settings.STATION_ID

def get_tag_dict(tag_id, restrict=None, org_id=None):
    params = {}
    params['id'] = tag_id
    if org_id:
        params['orgId'] = org_id
    else:
        params['orgID'] = public_org_id
    if restrict:
        params['requiredAssets'] = restrict
    return get_dict_from_story_api(params)
