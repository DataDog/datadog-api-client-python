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
    authn_mapping_id = "authn_mapping_id_example"  # str | The UUID of the AuthN Mapping.
    body = AuthNMappingUpdateRequest(
        data=AuthNMappingUpdateData(
            attributes=AuthNMappingUpdateAttributes(
                attribute_key="member-of",
                attribute_value="Development",
            ),
            id="3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
            relationships=AuthNMappingUpdateRelationships(
                role=RelationshipToRole(
                    data=RelationshipToRoleData(
                        id="3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
                        type=RolesType("roles"),
                    ),
                ),
            ),
            type=AuthNMappingsType("authn_mappings"),
        ),
    )  # AuthNMappingUpdateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Edit an AuthN Mapping
        api_response = api_instance.update_auth_n_mapping(authn_mapping_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthNMappingsApi->update_auth_n_mapping: %s\n" % e)
