"""
Update a permanent RUM retention filter returns "Updated" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RumRetentionFiltersApi
from datadog_api_client.v2.model.rum_cross_product_sampling_update import RumCrossProductSamplingUpdate
from datadog_api_client.v2.model.rum_permanent_retention_filter_id import RumPermanentRetentionFilterID
from datadog_api_client.v2.model.rum_permanent_retention_filter_type import RumPermanentRetentionFilterType
from datadog_api_client.v2.model.rum_permanent_retention_filter_update_attributes import (
    RumPermanentRetentionFilterUpdateAttributes,
)
from datadog_api_client.v2.model.rum_permanent_retention_filter_update_data import RumPermanentRetentionFilterUpdateData
from datadog_api_client.v2.model.rum_permanent_retention_filter_update_request import (
    RumPermanentRetentionFilterUpdateRequest,
)

body = RumPermanentRetentionFilterUpdateRequest(
    data=RumPermanentRetentionFilterUpdateData(
        attributes=RumPermanentRetentionFilterUpdateAttributes(
            cross_product_sampling=RumCrossProductSamplingUpdate(
                trace_enabled=True,
                trace_sample_rate=25.0,
            ),
        ),
        id=RumPermanentRetentionFilterID.SYNTHETICS_SESSIONS,
        type=RumPermanentRetentionFilterType.PERMANENT_RETENTION_FILTERS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersApi(api_client)
    response = api_instance.update_permanent_retention_filter(
        app_id="app_id", permanent_rf_id=RumPermanentRetentionFilterID.SYNTHETICS_SESSIONS, body=body
    )

    print(response)
