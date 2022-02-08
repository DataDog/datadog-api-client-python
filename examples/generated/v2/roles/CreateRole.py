import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import roles_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = roles_api.RolesApi(api_client)
    body = RoleCreateRequest(
        data=RoleCreateData(
            attributes=RoleCreateAttributes(
                name="developers",
            ),
            relationships=RoleRelationships(
                permissions=RelationshipToPermissions(
                    data=[
                        RelationshipToPermissionData(
                            id="id_example",
                            type=PermissionsType("permissions"),
                        ),
                    ],
                ),
                users=RelationshipToUsers(
                    data=[
                        RelationshipToUserData(
                            id="00000000-0000-0000-0000-000000000000",
                            type=UsersType("users"),
                        ),
                    ],
                ),
            ),
            type=RolesType("roles"),
        ),
    )  # RoleCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create role
        api_response = api_instance.create_role(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->create_role: %s\n" % e)
