"""
Create a Temporal Cloud OpenMetrics account returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.temporal_cloud_open_metrics_integration_api import TemporalCloudOpenMetricsIntegrationApi
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType
from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_bearer_token_auth_request import (
    TemporalCloudOpenMetricsIntegrationAccountBearerTokenAuthRequest,
)
from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_bearer_token_auth_type import (
    TemporalCloudOpenMetricsIntegrationAccountBearerTokenAuthType,
)
from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_create_attributes import (
    TemporalCloudOpenMetricsIntegrationAccountCreateAttributes,
)
from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_create_data import (
    TemporalCloudOpenMetricsIntegrationAccountCreateData,
)
from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_create_request import (
    TemporalCloudOpenMetricsIntegrationAccountCreateRequest,
)
from datadog_api_client.v2.model.temporal_cloud_open_metrics_integration_account_settings_request import (
    TemporalCloudOpenMetricsIntegrationAccountSettingsRequest,
)

body = TemporalCloudOpenMetricsIntegrationAccountCreateRequest(
    data=TemporalCloudOpenMetricsIntegrationAccountCreateData(
        attributes=TemporalCloudOpenMetricsIntegrationAccountCreateAttributes(
            authentication=TemporalCloudOpenMetricsIntegrationAccountBearerTokenAuthRequest(
                auth_type=TemporalCloudOpenMetricsIntegrationAccountBearerTokenAuthType.BEARER_TOKEN,
                token="your-token",
            ),
            name="temporal-cloud-prod",
            settings=TemporalCloudOpenMetricsIntegrationAccountSettingsRequest(
                include_opt_in_labels=False,
                namespaces_to_include="prod-*,billing.a1b2c",
            ),
        ),
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_temporal_cloud_open_metrics_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = TemporalCloudOpenMetricsIntegrationApi(api_client)
    response = api_instance.create_temporal_cloud_open_metrics_integration_account(body=body)

    print(response)
