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


class FindingLinearIssueResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "issue_id": (str,),
            "issue_key": (str,),
            "team_id": (str,),
            "url": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "issue_id": "issue_id",
        "issue_key": "issue_key",
        "team_id": "team_id",
        "url": "url",
    }

    def __init__(
        self_,
        account_id: Union[str, UnsetType] = unset,
        issue_id: Union[str, UnsetType] = unset,
        issue_key: Union[str, UnsetType] = unset,
        team_id: Union[str, UnsetType] = unset,
        url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Result of the Linear issue creation.

        :param account_id: Account ID of the Linear workspace.
        :type account_id: str, optional

        :param issue_id: Unique identifier of the Linear issue.
        :type issue_id: str, optional

        :param issue_key: Key of the Linear issue.
        :type issue_key: str, optional

        :param team_id: Team ID of the Linear issue.
        :type team_id: str, optional

        :param url: URL of the Linear issue.
        :type url: str, optional
        """
        if account_id is not unset:
            kwargs["account_id"] = account_id
        if issue_id is not unset:
            kwargs["issue_id"] = issue_id
        if issue_key is not unset:
            kwargs["issue_key"] = issue_key
        if team_id is not unset:
            kwargs["team_id"] = team_id
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)
