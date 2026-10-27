"""
Create a persistent email global variable returns a generated address
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_global_variable_request import SyntheticsGlobalVariableRequest

body = SyntheticsGlobalVariableRequest(
    name="PERSISTENT_EMAIL_EXAMPLESYNTHETIC",
    description="Persistent email variable",
    tags=[],
    is_email=True,
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.create_global_variable(body=body)

    print(response)
