import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import users_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    body = User(
        access_role=AccessRole("st"),
        disabled=False,
        email="test@datadoghq.com",
        handle="test@datadoghq.com",
        name="test user",
    )  # User | User object that needs to be created.

    # example passing only required values which don't have defaults set
    try:
        # Create a user
        api_response = api_instance.create_user(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
