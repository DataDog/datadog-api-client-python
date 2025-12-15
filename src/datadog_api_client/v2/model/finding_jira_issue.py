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
    from datadog_api_client.v2.model.finding_jira_issue_result import FindingJiraIssueResult


class FindingJiraIssue(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.finding_jira_issue_result import FindingJiraIssueResult

        return {
            "error_message": (str,),
            "result": (FindingJiraIssueResult,),
            "status": (str,),
        }

    attribute_map = {
        "error_message": "error_message",
        "result": "result",
        "status": "status",
    }

    def __init__(
        self_,
        error_message: Union[str, UnsetType] = unset,
        result: Union[FindingJiraIssueResult, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Jira issue associated with the case.

        :param error_message: Error message if the Jira issue creation failed.
        :type error_message: str, optional

        :param result: Result of the Jira issue creation.
        :type result: FindingJiraIssueResult, optional

        :param status: Status of the Jira issue creation. Can be "COMPLETED" if the Jira issue was created successfully, or "FAILED" if the Jira issue creation failed.
        :type status: str, optional
        """
        if error_message is not unset:
            kwargs["error_message"] = error_message
        if result is not unset:
            kwargs["result"] = result
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
