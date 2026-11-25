"""
Update a permanent RUM retention filter returns "Updated" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RUMRetentionFiltersApi
from datadog_api_client.v2.model.rum_cross_product_sampling_update import RUMCrossProductSamplingUpdate
from datadog_api_client.v2.model.rum_permanent_retention_filter_id import RUMPermanentRetentionFilterID
from datadog_api_client.v2.model.rum_permanent_retention_filter_type import RUMPermanentRetentionFilterType
from datadog_api_client.v2.model.rum_permanent_retention_filter_update_attributes import (
    RUMPermanentRetentionFilterUpdateAttributes,
)
from datadog_api_client.v2.model.rum_permanent_retention_filter_update_data import RUMPermanentRetentionFilterUpdateData
from datadog_api_client.v2.model.rum_permanent_retention_filter_update_request import (
    RUMPermanentRetentionFilterUpdateRequest,
)

body = RUMPermanentRetentionFilterUpdateRequest(
    data=RUMPermanentRetentionFilterUpdateData(
        attributes=RUMPermanentRetentionFilterUpdateAttributes(
            cross_product_sampling=RUMCrossProductSamplingUpdate(
                trace_enabled=True,
                trace_sample_rate=25.0,
            ),
        ),
        id=RUMPermanentRetentionFilterID.SYNTHETICS_SESSIONS,
        type=RUMPermanentRetentionFilterType.PERMANENT_RETENTION_FILTERS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RUMRetentionFiltersApi(api_client)
    response = api_instance.update_permanent_retention_filter(
        app_id="app_id", permanent_rf_id=RUMPermanentRetentionFilterID.SYNTHETICS_SESSIONS, body=body
    )

    print(response)
