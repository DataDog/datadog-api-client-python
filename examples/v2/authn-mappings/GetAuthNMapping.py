"""
Get an AuthN Mapping by UUID returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.authn_mappings_api import AuthNMappingsApi

# there is a valid "authn_mapping" in the system
AUTHN_MAPPING_DATA_ID = environ["AUTHN_MAPPING_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuthNMappingsApi(api_client)
    response = api_instance.get_authn_mapping(
        authn_mapping_id=AUTHN_MAPPING_DATA_ID,
    )

    print(response)
