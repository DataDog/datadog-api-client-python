# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.issue_pull_request_reason import IssuePullRequestReason


class IssuePullRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.issue_pull_request_reason import IssuePullRequestReason

        return {
            "closed_at": (datetime,),
            "linked_at": (datetime,),
            "merged_at": (datetime,),
            "reason": (IssuePullRequestReason,),
            "url": (str,),
        }

    attribute_map = {
        "closed_at": "closed_at",
        "linked_at": "linked_at",
        "merged_at": "merged_at",
        "reason": "reason",
        "url": "url",
    }

    def __init__(
        self_,
        closed_at: Union[datetime, UnsetType] = unset,
        linked_at: Union[datetime, UnsetType] = unset,
        merged_at: Union[datetime, UnsetType] = unset,
        reason: Union[IssuePullRequestReason, UnsetType] = unset,
        url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object containing the information of a pull request linked to an issue.

        :param closed_at: Timestamp of when the pull request was closed. Omitted if the pull request is not closed.
        :type closed_at: datetime, optional

        :param linked_at: Timestamp of when the pull request was linked to the issue.
        :type linked_at: datetime, optional

        :param merged_at: Timestamp of when the pull request was merged. Omitted if the pull request is not merged.
        :type merged_at: datetime, optional

        :param reason: Why the pull request is linked to the issue. ``fix`` means the pull request fixes the issue, and ``trigger`` means the pull request introduced the issue.
        :type reason: IssuePullRequestReason, optional

        :param url: URL of the pull request.
        :type url: str, optional
        """
        if closed_at is not unset:
            kwargs["closed_at"] = closed_at
        if linked_at is not unset:
            kwargs["linked_at"] = linked_at
        if merged_at is not unset:
            kwargs["merged_at"] = merged_at
        if reason is not unset:
            kwargs["reason"] = reason
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)
