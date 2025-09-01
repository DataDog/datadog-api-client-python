# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.issue_case_jira_issue_result import IssueCaseJiraIssueResult


class IssueCaseJiraIssue(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_case_jira_issue_result import IssueCaseJiraIssueResult

        return {
            "result": (IssueCaseJiraIssueResult,),
            "status": (str,),
        }

    attribute_map = {
        "result": "result",
        "status": "status",
    }

    def __init__(
        self_,
        result: Union[IssueCaseJiraIssueResult, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Jira issue of the case.

        :param result: Contains the identifiers and URL for a successfully created Jira issue.
        :type result: IssueCaseJiraIssueResult, optional

        :param status: Creation status of the Jira issue.
        :type status: str, optional
        """
        if result is not unset:
            kwargs["result"] = result
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
