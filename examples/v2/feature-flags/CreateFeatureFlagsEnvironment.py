"""
Create an environment returns "Created" response
"""

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
            name="Test Environment Example-Feature-Flag",
            queries=[
                "test-Example-Feature-Flag",
                "env-Example-Feature-Flag",
            ],
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.create_feature_flags_environment(body=body)

    print(response)
