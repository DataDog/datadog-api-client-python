"""
Update a hardcoded retention filter returns "Updated" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_hardcoded_api import RUMRetentionFiltersHardcodedApi
from datadog_api_client.v2.model.rum_hardcoded_cross_product_sampling_update import (
    RumHardcodedCrossProductSamplingUpdate,
)
from datadog_api_client.v2.model.rum_hardcoded_retention_filter_type import RumHardcodedRetentionFilterType
from datadog_api_client.v2.model.rum_hardcoded_retention_filter_update_attributes import (
    RumHardcodedRetentionFilterUpdateAttributes,
)
from datadog_api_client.v2.model.rum_hardcoded_retention_filter_update_data import RumHardcodedRetentionFilterUpdateData
from datadog_api_client.v2.model.rum_hardcoded_retention_filter_update_request import (
    RumHardcodedRetentionFilterUpdateRequest,
)

body = RumHardcodedRetentionFilterUpdateRequest(
    data=RumHardcodedRetentionFilterUpdateData(
        id="REPLACE.ME",
        type=RumHardcodedRetentionFilterType.HARDCODED_RETENTION_FILTERS,
        attributes=RumHardcodedRetentionFilterUpdateAttributes(
            cross_product_sampling=RumHardcodedCrossProductSamplingUpdate(
                session_replay_sample_rate=50.0,
                session_replay_enabled=True,
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMRetentionFiltersHardcodedApi(api_client)
    response = api_instance.update_hardcoded_retention_filter(
        app_id="Example-RUM-Retention-Filters-Hardcoded", rf_id="Example-RUM-Retention-Filters-Hardcoded", body=body
    )

    print(response)
