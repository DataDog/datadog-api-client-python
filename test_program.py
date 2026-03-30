"""Test PAT auth using the EXISTING access_token/AuthZ (OAuth2) support on master."""

import json
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi

pat = "ddpat_REPLACE_WITH_YOUR_PAT"

configuration = Configuration(
    host="https://dd.datad0g.com",
    access_token=pat,
)
configuration.debug = True

with ApiClient(configuration) as api_client:
    api = UsersApi(api_client)
    response = api.list_users(page_size=2)
    print("Response from UsersApi.list_users:")
    print(json.dumps(response.to_dict(), indent=2, default=str))
