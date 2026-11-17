"""
Update a CoreWeave integration account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.core_weave_integration_api import CoreWeaveIntegrationApi
from datadog_api_client.v2.model.core_weave_cloud_integration_account_api_token_auth_type import (
    CoreWeaveCloudIntegrationAccountAPITokenAuthType,
)
from datadog_api_client.v2.model.core_weave_cloud_integration_account_api_token_auth_update import (
    CoreWeaveCloudIntegrationAccountAPITokenAuthUpdate,
)
from datadog_api_client.v2.model.core_weave_cloud_integration_account_settings_update import (
    CoreWeaveCloudIntegrationAccountSettingsUpdate,
)
from datadog_api_client.v2.model.core_weave_cloud_integration_account_update_attributes import (
    CoreWeaveCloudIntegrationAccountUpdateAttributes,
)
from datadog_api_client.v2.model.core_weave_cloud_integration_account_update_data import (
    CoreWeaveCloudIntegrationAccountUpdateData,
)
from datadog_api_client.v2.model.core_weave_cloud_integration_account_update_request import (
    CoreWeaveCloudIntegrationAccountUpdateRequest,
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

body = CoreWeaveCloudIntegrationAccountUpdateRequest(
    data=CoreWeaveCloudIntegrationAccountUpdateData(
        attributes=CoreWeaveCloudIntegrationAccountUpdateAttributes(
            authentication=CoreWeaveCloudIntegrationAccountAPITokenAuthUpdate(
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
            settings=CoreWeaveCloudIntegrationAccountSettingsUpdate(
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
        id="f7a8b9c0-d1e2-4f3a-9b4c-5d6e7f8091a2",
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_core_weave_cloud_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = CoreWeaveIntegrationApi(api_client)
    response = api_instance.update_core_weave_cloud_integration_account(account_id="account_id", body=body)

    print(response)
