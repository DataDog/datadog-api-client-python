"""
Update a permanent retention filter returns "Updated" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_permanent_api import RumRetentionFiltersPermanentApi
from datadog_api_client.v2.model.rum_permanent_cross_product_sampling_update import (
    RumPermanentCrossProductSamplingUpdate,
)
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
        id="default_replays",
        type=RumPermanentRetentionFilterType.PERMANENT_RETENTION_FILTERS,
        attributes=RumPermanentRetentionFilterUpdateAttributes(
            cross_product_sampling=RumPermanentCrossProductSamplingUpdate(
                trace_sample_rate=100.0,
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RumRetentionFiltersPermanentApi(api_client)
    response = api_instance.update_permanent_retention_filter(
        app_id="a33671aa-24fd-4dcd-ba4b-5bbdbafe7690", rf_id="default_replays", body=body
    )

    print(response)
