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


class CaseViewCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "np_rule_id": (str,),
            "project_id": (str,),
            "query": (str,),
        }

    attribute_map = {
        "name": "name",
        "np_rule_id": "np_rule_id",
        "project_id": "project_id",
        "query": "query",
    }

    def __init__(self_, name: str, project_id: str, query: str, np_rule_id: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes required to create a case view.

        :param name: The name of the view.
        :type name: str

        :param np_rule_id: The identifier of a notification rule linked to this view. When set, users subscribed to the view receive alerts for matching cases.
        :type np_rule_id: str, optional

        :param project_id: The UUID of the project this view belongs to. Views are scoped to a single project.
        :type project_id: str

        :param query: The query used to filter cases in this view.
        :type query: str
        """
        if np_rule_id is not unset:
            kwargs["np_rule_id"] = np_rule_id
        super().__init__(kwargs)

        self_.name = name
        self_.project_id = project_id
        self_.query = query
