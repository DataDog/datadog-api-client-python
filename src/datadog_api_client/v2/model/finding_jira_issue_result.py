# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class FindingJiraIssueResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "issue_id": (str,),
            "issue_key": (str,),
            "issue_url": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "issue_id": "issue_id",
        "issue_key": "issue_key",
        "issue_url": "issue_url",
    }

    def __init__(
        self_,
        account_id: Union[str, UnsetType] = unset,
        issue_id: Union[str, UnsetType] = unset,
        issue_key: Union[str, UnsetType] = unset,
        issue_url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Result of the Jira issue creation.

        :param account_id: Account ID of the Jira issue.
        :type account_id: str, optional

        :param issue_id: Unique identifier of the Jira issue.
        :type issue_id: str, optional

        :param issue_key: Key of the Jira issue.
        :type issue_key: str, optional

        :param issue_url: URL of the Jira issue.
        :type issue_url: str, optional
        """
        if account_id is not unset:
            kwargs["account_id"] = account_id
        if issue_id is not unset:
            kwargs["issue_id"] = issue_id
        if issue_key is not unset:
            kwargs["issue_key"] = issue_key
        if issue_url is not unset:
            kwargs["issue_url"] = issue_url
        super().__init__(kwargs)
