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


class JiraIssueResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "issue_id": (str,),
            "issue_key": (str,),
            "issue_url": (str,),
            "project_key": (str,),
        }

    attribute_map = {
        "issue_id": "issue_id",
        "issue_key": "issue_key",
        "issue_url": "issue_url",
        "project_key": "project_key",
    }

    def __init__(
        self_,
        issue_id: Union[str, UnsetType] = unset,
        issue_key: Union[str, UnsetType] = unset,
        issue_url: Union[str, UnsetType] = unset,
        project_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Jira issue information

        :param issue_id: Jira issue ID
        :type issue_id: str, optional

        :param issue_key: Jira issue key
        :type issue_key: str, optional

        :param issue_url: Jira issue URL
        :type issue_url: str, optional

        :param project_key: Jira project key
        :type project_key: str, optional
        """
        if issue_id is not unset:
            kwargs["issue_id"] = issue_id
        if issue_key is not unset:
            kwargs["issue_key"] = issue_key
        if issue_url is not unset:
            kwargs["issue_url"] = issue_url
        if project_key is not unset:
            kwargs["project_key"] = project_key
        super().__init__(kwargs)
