"""
Aggregate cases returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_aggregate_group_by import CaseAggregateGroupBy
from datadog_api_client.v2.model.case_aggregate_request import CaseAggregateRequest
from datadog_api_client.v2.model.case_aggregate_request_attributes import CaseAggregateRequestAttributes
from datadog_api_client.v2.model.case_aggregate_request_data import CaseAggregateRequestData
from datadog_api_client.v2.model.case_aggregate_resource_type import CaseAggregateResourceType

body = CaseAggregateRequest(
    data=CaseAggregateRequestData(
        attributes=CaseAggregateRequestAttributes(
            group_by=CaseAggregateGroupBy(
                groups=[
                    "status",
                ],
                limit=14,
            ),
            query_filter="service:case-api",
        ),
        type=CaseAggregateResourceType.AGGREGATE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.aggregate_cases(body=body)

    print(response)
