"""
Get a list of failure events returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dora_metrics_api import DORAMetricsApi
from datadog_api_client.v2.model.dora_list_failures_request import DORAListFailuresRequest
from datadog_api_client.v2.model.dora_list_failures_request_attributes import DORAListFailuresRequestAttributes
from datadog_api_client.v2.model.dora_list_failures_request_data import DORAListFailuresRequestData
from datadog_api_client.v2.model.dora_list_failures_request_data_type import DORAListFailuresRequestDataType
from datetime import datetime
from dateutil.tz import tzutc

body = DORAListFailuresRequest(
    data=DORAListFailuresRequestData(
        attributes=DORAListFailuresRequestAttributes(
            _from=datetime(2025, 3, 23, 0, 0, tzinfo=tzutc()),
            limit=1,
            to=datetime(2025, 3, 24, 0, 0, tzinfo=tzutc()),
        ),
        type=DORAListFailuresRequestDataType.DORA_FAILURES_LIST_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DORAMetricsApi(api_client)
    response = api_instance.list_dora_failures(body=body)

    print(response)
