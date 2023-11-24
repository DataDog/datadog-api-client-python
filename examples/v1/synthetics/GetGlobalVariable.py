"""
Get a global variable returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi

# there is a valid "synthetics_global_variable" in the system
SYNTHETICS_GLOBAL_VARIABLE_ID = environ["SYNTHETICS_GLOBAL_VARIABLE_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.get_global_variable(
        variable_id=SYNTHETICS_GLOBAL_VARIABLE_ID,
    )

    print(response)
