import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import auth_n_mappings_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_n_mappings_api.AuthNMappingsApi(api_client)
    body = AuthNMappingCreateRequest(
        data=AuthNMappingCreateData(
            attributes=AuthNMappingCreateAttributes(
                attribute_key="member-of",
                attribute_value="Development",
            ),
            relationships=AuthNMappingCreateRelationships(
                role=RelationshipToRole(
                    data=RelationshipToRoleData(
                        id="3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
                        type=RolesType("roles"),
                    ),
                ),
            ),
            type=AuthNMappingsType("authn_mappings"),
        ),
    )  # AuthNMappingCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create an AuthN Mapping
        api_response = api_instance.create_auth_n_mapping(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthNMappingsApi->create_auth_n_mapping: %s\n" % e)
