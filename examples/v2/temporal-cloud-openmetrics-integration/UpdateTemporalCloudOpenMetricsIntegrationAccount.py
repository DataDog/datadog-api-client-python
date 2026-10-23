"""
Update a Temporal Cloud OpenMetrics account returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.temporal_cloud_open_metrics_integration_api import TemporalCloudOpenMetricsIntegrationApi
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType
from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_bearer_token_auth_type import (
    TemporalCloudOpenMetricsIntegrationAccountBearerTokenAuthType,
)
from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_bearer_token_auth_update import (
    TemporalCloudOpenMetricsIntegrationAccountBearerTokenAuthUpdate,
)
from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_settings_update import (
    TemporalCloudOpenMetricsIntegrationAccountSettingsUpdate,
)
from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_update_attributes import (
    TemporalCloudOpenMetricsIntegrationAccountUpdateAttributes,
)
from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_update_data import (
    TemporalCloudOpenMetricsIntegrationAccountUpdateData,
)
from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_update_request import (
    TemporalCloudOpenMetricsIntegrationAccountUpdateRequest,
)

body = TemporalCloudOpenMetricsIntegrationAccountUpdateRequest(
    data=TemporalCloudOpenMetricsIntegrationAccountUpdateData(
        attributes=TemporalCloudOpenMetricsIntegrationAccountUpdateAttributes(
            authentication=TemporalCloudOpenMetricsIntegrationAccountBearerTokenAuthUpdate(
                auth_type=TemporalCloudOpenMetricsIntegrationAccountBearerTokenAuthType.BEARER_TOKEN,
                token="your-token",
            ),
            name="temporal-cloud-prod",
            settings=TemporalCloudOpenMetricsIntegrationAccountSettingsUpdate(
                include_opt_in_labels=False,
                namespaces_to_include="prod-*,billing.a1b2c",
            ),
        ),
        id="7c2d4e91-5a3b-4f68-b0e2-9d1f6a8c3e57",
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_temporal_cloud_open_metrics_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = TemporalCloudOpenMetricsIntegrationApi(api_client)
    response = api_instance.update_temporal_cloud_open_metrics_integration_account(account_id="account_id", body=body)

    print(response)
