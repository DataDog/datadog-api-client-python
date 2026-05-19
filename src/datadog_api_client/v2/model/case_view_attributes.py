# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class CaseViewAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "modified_at": (datetime,),
            "name": (str,),
            "np_rule_id": (str,),
            "query": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "modified_at": "modified_at",
        "name": "name",
        "np_rule_id": "np_rule_id",
        "query": "query",
    }
    read_only_vars = {
        "created_at",
        "modified_at",
    }

    def __init__(
        self_,
        created_at: datetime,
        name: str,
        query: str,
        modified_at: Union[datetime, UnsetType] = unset,
        np_rule_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a case view, including the filter query and optional notification rule.

        :param created_at: Timestamp when the view was created.
        :type created_at: datetime

        :param modified_at: Timestamp when the view was last modified.
        :type modified_at: datetime, optional

        :param name: A human-readable name for the view, displayed in the Case Management UI.
        :type name: str

        :param np_rule_id: The identifier of a notification rule linked to this view. When set, users subscribed to the view receive alerts for matching cases.
        :type np_rule_id: str, optional

        :param query: The search query that determines which cases appear in this view. Uses the same syntax as the Case Management search bar (for example, ``status:open priority:P1`` ).
        :type query: str
        """
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if np_rule_id is not unset:
            kwargs["np_rule_id"] = np_rule_id
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.name = name
        self_.query = query
