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
    from datadog_api_client.v2.model.issue_case_linear_issue_result import IssueCaseLinearIssueResult


class IssueCaseLinearIssue(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_case_linear_issue_result import IssueCaseLinearIssueResult

        return {
            "error_message": (str,),
            "result": (IssueCaseLinearIssueResult,),
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
        result: Union[IssueCaseLinearIssueResult, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Linear issue of the case.

        :param error_message: Error message set when the Linear issue creation fails.
        :type error_message: str, optional

        :param result: Contains the identifiers and URL for a successfully created Linear issue.
        :type result: IssueCaseLinearIssueResult, optional

        :param status: Creation status of the Linear issue.
        :type status: str, optional
        """
        if error_message is not unset:
            kwargs["error_message"] = error_message
        if result is not unset:
            kwargs["result"] = result
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
