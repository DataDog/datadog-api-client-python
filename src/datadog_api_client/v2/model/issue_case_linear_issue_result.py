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


class IssueCaseLinearIssueResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "issue_id": (str,),
            "issue_key": (str,),
            "issue_url": (str,),
            "team_id": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "issue_id": "issue_id",
        "issue_key": "issue_key",
        "issue_url": "issue_url",
        "team_id": "team_id",
    }

    def __init__(
        self_,
        account_id: Union[str, UnsetType] = unset,
        issue_id: Union[str, UnsetType] = unset,
        issue_key: Union[str, UnsetType] = unset,
        issue_url: Union[str, UnsetType] = unset,
        team_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Contains the identifiers and URL for a successfully created Linear issue.

        :param account_id: Linear account identifier.
        :type account_id: str, optional

        :param issue_id: Linear issue identifier.
        :type issue_id: str, optional

        :param issue_key: Linear issue key.
        :type issue_key: str, optional

        :param issue_url: Linear issue URL.
        :type issue_url: str, optional

        :param team_id: Linear team identifier.
        :type team_id: str, optional
        """
        if account_id is not unset:
            kwargs["account_id"] = account_id
        if issue_id is not unset:
            kwargs["issue_id"] = issue_id
        if issue_key is not unset:
            kwargs["issue_key"] = issue_key
        if issue_url is not unset:
            kwargs["issue_url"] = issue_url
        if team_id is not unset:
            kwargs["team_id"] = team_id
        super().__init__(kwargs)
