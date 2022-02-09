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
    role_id = "role_id_example"  # str | The ID of the role.
    body = RelationshipToUser(
        data=RelationshipToUserData(
            id="00000000-0000-0000-0000-000000000000",
            type=UsersType("users"),
        ),
    )  # RelationshipToUser | 

    # example passing only required values which don't have defaults set
    try:
        # Add a user to a role
        api_response = api_instance.add_user_to_role(role_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->add_user_to_role: %s\n" % e)
