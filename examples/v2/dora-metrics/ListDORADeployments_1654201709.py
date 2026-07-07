"""
Get a list of deployment events returns deployments with date-time timestamps
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dora_metrics_api import DORAMetricsApi
from datadog_api_client.v2.model.dora_list_deployments_request import DORAListDeploymentsRequest
from datadog_api_client.v2.model.dora_list_deployments_request_attributes import DORAListDeploymentsRequestAttributes
from datadog_api_client.v2.model.dora_list_deployments_request_data import DORAListDeploymentsRequestData
from datadog_api_client.v2.model.dora_list_deployments_request_data_type import DORAListDeploymentsRequestDataType
from datetime import datetime
from dateutil.tz import tzutc

body = DORAListDeploymentsRequest(
    data=DORAListDeploymentsRequestData(
        attributes=DORAListDeploymentsRequestAttributes(
            _from=datetime(2023, 8, 31, 0, 0, tzinfo=tzutc()),
            to=datetime(2023, 9, 1, 0, 0, tzinfo=tzutc()),
        ),
        type=DORAListDeploymentsRequestDataType.DORA_DEPLOYMENTS_LIST_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DORAMetricsApi(api_client)
    response = api_instance.list_dora_deployments(body=body)

    print(response)
