"""
Create an AuthN Mapping returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.authn_mappings_api import AuthNMappingsApi
from datadog_api_client.v2.model.authn_mapping_create_request import AuthNMappingCreateRequestJSON

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

body = AuthNMappingCreateRequestJSON(
    attribute_key="exampleauthnmapping",
    attribute_value="Example-AuthN-Mapping",
    role="string",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AuthNMappingsApi(api_client)
    response = api_instance.create_authn_mapping(body=body)

    print(response)
