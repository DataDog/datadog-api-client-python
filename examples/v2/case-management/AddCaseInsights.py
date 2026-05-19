"""
Add insights to a case returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_insight import CaseInsight
from datadog_api_client.v2.model.case_insight_type import CaseInsightType
from datadog_api_client.v2.model.case_insights_attributes import CaseInsightsAttributes
from datadog_api_client.v2.model.case_insights_data import CaseInsightsData
from datadog_api_client.v2.model.case_insights_request import CaseInsightsRequest
from datadog_api_client.v2.model.case_resource_type import CaseResourceType

body = CaseInsightsRequest(
    data=CaseInsightsData(
        attributes=CaseInsightsAttributes(
            insights=[
                CaseInsight(
                    ref="/monitors/12345?q=total",
                    resource_id="12345",
                    type=CaseInsightType.SECURITY_SIGNAL,
                ),
            ],
        ),
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["add_case_insights"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.add_case_insights(case_id="case_id", body=body)

    print(response)
