"""
Update resource filters returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.resource_filter_attributes import ResourceFilterAttributes
from datadog_api_client.v2.model.resource_filter_request_type import ResourceFilterRequestType
from datadog_api_client.v2.model.update_resource_evaluation_filters_request import (
    UpdateResourceEvaluationFiltersRequest,
)
from datadog_api_client.v2.model.update_resource_evaluation_filters_request_data import (
    UpdateResourceEvaluationFiltersRequestData,
)

body = UpdateResourceEvaluationFiltersRequest(
    data=UpdateResourceEvaluationFiltersRequestData(
        attributes=ResourceFilterAttributes(
            cloud_provider=dict(
                aws=dict(
                    aws_account_id=[
                        "tag1:v1",
                    ],
                ),
            ),
        ),
        id="csm_resource_filter",
        type=ResourceFilterRequestType.CSM_RESOURCE_FILTER,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.update_resource_evaluation_filters(body=body)

    print(response)
