import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v2 import ApiClient, ApiException, Configuration
from datadog_api_client.v2.api import users_api
from datadog_api_client.v2.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    body = UserCreateRequest(
        data=UserCreateData(
            attributes=UserCreateAttributes(
                email="jane.doe@example.com",
                name="name_example",
                title="title_example",
            ),
            relationships=UserRelationships(
                roles=RelationshipToRoles(
                    data=[
                        RelationshipToRoleData(
                            id="3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
                            type=RolesType("roles"),
                        ),
                    ],
                ),
            ),
            type=UsersType("users"),
        ),
    )  # UserCreateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a user
        api_response = api_instance.create_user(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
