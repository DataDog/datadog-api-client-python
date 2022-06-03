"""
List all AuthN Mappings returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.authn_mappings_api import AuthNMappingsApi

# there is a valid "authn_mapping" in the system
AUTHN_MAPPING_DATA_ATTRIBUTES_ATTRIBUTE_KEY = environ["AUTHN_MAPPING_DATA_ATTRIBUTES_ATTRIBUTE_KEY"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuthNMappingsApi(api_client)
    response = api_instance.list_authn_mappings(
        filter=AUTHN_MAPPING_DATA_ATTRIBUTES_ATTRIBUTE_KEY,
    )

    print(response)
