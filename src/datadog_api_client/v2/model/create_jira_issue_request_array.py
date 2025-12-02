# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_jira_issue_request_data import CreateJiraIssueRequestData
    from datadog_api_client.v2.model.create_jira_issue_request_array_included import CreateJiraIssueRequestArrayIncluded
    from datadog_api_client.v2.model.create_case_request_data import CreateCaseRequestData
    from datadog_api_client.v2.model.case_management_project_data import CaseManagementProjectData
    from datadog_api_client.v2.model.finding_data import FindingData


class CreateJiraIssueRequestArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_jira_issue_request_data import CreateJiraIssueRequestData
        from datadog_api_client.v2.model.create_jira_issue_request_array_included import (
            CreateJiraIssueRequestArrayIncluded,
        )

        return {
            "data": ([CreateJiraIssueRequestData],),
            "included": ([CreateJiraIssueRequestArrayIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: List[CreateJiraIssueRequestData],
        included: Union[
            List[
                Union[
                    CreateJiraIssueRequestArrayIncluded, CreateCaseRequestData, CaseManagementProjectData, FindingData
                ]
            ],
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        List of requests to create Jira issues for security findings.

        :param data:
        :type data: [CreateJiraIssueRequestData]

        :param included:
        :type included: [CreateJiraIssueRequestArrayIncluded], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
