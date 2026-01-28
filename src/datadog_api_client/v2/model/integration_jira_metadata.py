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


class IntegrationJiraMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "issue_type_id": (str,),
            "project_id": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "issue_type_id": "issue_type_id",
        "project_id": "project_id",
    }

    def __init__(
        self_,
        account_id: Union[str, UnsetType] = unset,
        issue_type_id: Union[str, UnsetType] = unset,
        project_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param account_id:
        :type account_id: str, optional

        :param issue_type_id:
        :type issue_type_id: str, optional

        :param project_id:
        :type project_id: str, optional
        """
        if account_id is not unset:
            kwargs["account_id"] = account_id
        if issue_type_id is not unset:
            kwargs["issue_type_id"] = issue_type_id
        if project_id is not unset:
            kwargs["project_id"] = project_id
        super().__init__(kwargs)
