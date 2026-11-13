"""
Create an environment with full evaluation data false returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from datadog_api_client.v2.model.create_environment_attributes import CreateEnvironmentAttributes
from datadog_api_client.v2.model.create_environment_data import CreateEnvironmentData
from datadog_api_client.v2.model.create_environment_data_type import CreateEnvironmentDataType
from datadog_api_client.v2.model.create_environment_request import CreateEnvironmentRequest

body = CreateEnvironmentRequest(
    data=CreateEnvironmentData(
        type=CreateEnvironmentDataType.ENVIRONMENTS,
        attributes=CreateEnvironmentAttributes(
            name="Evaluation Privacy Example-Feature-Flag",
            queries=[
                "privacy-example-feature-flag",
            ],
            observe_full_evaluation_data=False,
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.create_feature_flags_environment(body=body)

    print(response)
