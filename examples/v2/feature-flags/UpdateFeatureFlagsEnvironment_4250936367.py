"""
Update an environment to preserve enabled full evaluation data when omitted returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.feature_flags_api import FeatureFlagsApi
from datadog_api_client.v2.model.update_environment_attributes import UpdateEnvironmentAttributes
from datadog_api_client.v2.model.update_environment_data import UpdateEnvironmentData
from datadog_api_client.v2.model.update_environment_data_type import UpdateEnvironmentDataType
from datadog_api_client.v2.model.update_environment_request import UpdateEnvironmentRequest

# there is a valid "environment_with_full_evaluation_data" in the system
ENVIRONMENT_WITH_FULL_EVALUATION_DATA_DATA_ID = environ["ENVIRONMENT_WITH_FULL_EVALUATION_DATA_DATA_ID"]

body = UpdateEnvironmentRequest(
    data=UpdateEnvironmentData(
        type=UpdateEnvironmentDataType.ENVIRONMENTS,
        attributes=UpdateEnvironmentAttributes(
            name="Updated Privacy Example-Feature-Flag",
            queries=[
                "updated-privacy-example-feature-flag",
            ],
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = FeatureFlagsApi(api_client)
    response = api_instance.update_feature_flags_environment(
        environment_id=ENVIRONMENT_WITH_FULL_EVALUATION_DATA_DATA_ID, body=body
    )

    print(response)
