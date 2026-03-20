"""
Update an environment returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from datadog_api_client.v2.model.update_environment_attributes import UpdateEnvironmentAttributes
from datadog_api_client.v2.model.update_environment_data import UpdateEnvironmentData
from datadog_api_client.v2.model.update_environment_data_type import UpdateEnvironmentDataType
from datadog_api_client.v2.model.update_environment_request import UpdateEnvironmentRequest

# there is a valid "environment" in the system
ENVIRONMENT_DATA_ID = environ["ENVIRONMENT_DATA_ID"]

body = UpdateEnvironmentRequest(
    data=UpdateEnvironmentData(
        type=UpdateEnvironmentDataType.ENVIRONMENTS,
        attributes=UpdateEnvironmentAttributes(
            name="Updated Test Environment Example-Feature-Flag",
            queries=[
                "updated-Example-Feature-Flag",
                "live-Example-Feature-Flag",
            ],
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.update_feature_flags_environment(environment_id=ENVIRONMENT_DATA_ID, body=body)

    print(response)
