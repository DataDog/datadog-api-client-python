"""
Create a CoreWeave integration account returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.core_weave_integration_api import CoreWeaveIntegrationApi
from datadog_api_client.v2.model.core_weave_cloud_integration_account_api_token_auth_request import (
    CoreWeaveCloudIntegrationAccountAPITokenAuthRequest,
)
from datadog_api_client.v2.model.core_weave_cloud_integration_account_api_token_auth_type import (
    CoreWeaveCloudIntegrationAccountAPITokenAuthType,
)
from datadog_api_client.v2.model.core_weave_cloud_integration_account_create_attributes import (
    CoreWeaveCloudIntegrationAccountCreateAttributes,
)
from datadog_api_client.v2.model.core_weave_cloud_integration_account_create_data import (
    CoreWeaveCloudIntegrationAccountCreateData,
)
from datadog_api_client.v2.model.core_weave_cloud_integration_account_create_request import (
    CoreWeaveCloudIntegrationAccountCreateRequest,
)
from datadog_api_client.v2.model.core_weave_cloud_integration_account_settings_request import (
    CoreWeaveCloudIntegrationAccountSettingsRequest,
)
from datadog_api_client.v2.model.core_weave_cloud_integration_dataflows_request import (
    CoreWeaveCloudIntegrationDataflowsRequest,
)
from datadog_api_client.v2.model.core_weave_cloud_logs_integration_dataflow_request import (
    CoreWeaveCloudLogsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.core_weave_cloud_metrics_integration_dataflow_request import (
    CoreWeaveCloudMetricsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType

body = CoreWeaveCloudIntegrationAccountCreateRequest(
    data=CoreWeaveCloudIntegrationAccountCreateData(
        attributes=CoreWeaveCloudIntegrationAccountCreateAttributes(
            authentication=CoreWeaveCloudIntegrationAccountAPITokenAuthRequest(
                api_token="CW-SECRET-xxxxxxxxxxxxxxxxxxxx",
                auth_type=CoreWeaveCloudIntegrationAccountAPITokenAuthType.COREWEAVE_API_TOKEN,
            ),
            dataflows=CoreWeaveCloudIntegrationDataflowsRequest(
                coreweave_cloud_logs=CoreWeaveCloudLogsIntegrationDataflowRequest(
                    enabled=True,
                ),
                coreweave_cloud_metrics=CoreWeaveCloudMetricsIntegrationDataflowRequest(
                    enabled=True,
                ),
            ),
            name="coreweave-prod",
            settings=CoreWeaveCloudIntegrationAccountSettingsRequest(
                account_tags=[
                    "env:prod",
                    "team:gpu",
                ],
                cluster_filters=[
                    "cluster:prod-*",
                    "!cluster:dev",
                ],
            ),
        ),
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_core_weave_cloud_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = CoreWeaveIntegrationApi(api_client)
    response = api_instance.create_core_weave_cloud_integration_account(body=body)

    print(response)
