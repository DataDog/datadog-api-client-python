"""
Edit an AuthN Mapping returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.authn_mappings_api import AuthNMappingsApi
from datadog_api_client.v2.model.authn_mapping_update_request import AuthNMappingUpdateRequestJSON

# there is a valid "authn_mapping" in the system
AUTHN_MAPPING_DATA_ID = environ["AUTHN_MAPPING_DATA_ID"]

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = AuthNMappingUpdateRequestJSON(
    id=AUTHN_MAPPING_DATA_ID,
    attribute_key="member-of",
    attribute_value="Development",
    role="string",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuthNMappingsApi(api_client)
    response = api_instance.update_authn_mapping(authn_mapping_id=AUTHN_MAPPING_DATA_ID, body=body)

    print(response)
