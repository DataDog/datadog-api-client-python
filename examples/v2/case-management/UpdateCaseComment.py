"""
Update case comment returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_resource_type import CaseResourceType
from datadog_api_client.v2.model.case_update_comment import CaseUpdateComment
from datadog_api_client.v2.model.case_update_comment_attributes import CaseUpdateCommentAttributes
from datadog_api_client.v2.model.case_update_comment_request import CaseUpdateCommentRequest

body = CaseUpdateCommentRequest(
    data=CaseUpdateComment(
        attributes=CaseUpdateCommentAttributes(
            comment="Updated comment text",
        ),
        type=CaseResourceType.CASE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_case_comment"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    api_instance.update_case_comment(case_id="case_id", cell_id="cell_id", body=body)
