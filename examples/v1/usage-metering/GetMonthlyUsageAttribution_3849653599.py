"""
Paginate monthly usage attribution
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.usage_metering_api import UsageMeteringApi
from datadog_api_client.v1.model.monthly_usage_attribution_supported_metrics import (
    MonthlyUsageAttributionSupportedMetrics,
)

# there is a valid "monthly_usage_attribution" response
MONTHLY_USAGE_ATTRIBUTION_METADATA_PAGINATION_NEXT_RECORD_ID = environ[
    "MONTHLY_USAGE_ATTRIBUTION_METADATA_PAGINATION_NEXT_RECORD_ID"
]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_monthly_usage_attribution(
        start_month=(datetime.now() + relativedelta(days=-3)),
        fields=MonthlyUsageAttributionSupportedMetrics.INFRA_HOST_USAGE,
        next_record_id=MONTHLY_USAGE_ATTRIBUTION_METADATA_PAGINATION_NEXT_RECORD_ID,
    )

    print(response)
