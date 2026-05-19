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


class CaseViewUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "np_rule_id": (str,),
            "query": (str,),
        }

    attribute_map = {
        "name": "name",
        "np_rule_id": "np_rule_id",
        "query": "query",
    }

    def __init__(
        self_,
        name: Union[str, UnsetType] = unset,
        np_rule_id: Union[str, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes that can be updated on a case view. All fields are optional; only provided fields are changed.

        :param name: The name of the view.
        :type name: str, optional

        :param np_rule_id: The identifier of a notification rule linked to this view. When set, users subscribed to the view receive alerts for matching cases.
        :type np_rule_id: str, optional

        :param query: The query used to filter cases in this view.
        :type query: str, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if np_rule_id is not unset:
            kwargs["np_rule_id"] = np_rule_id
        if query is not unset:
            kwargs["query"] = query
        super().__init__(kwargs)
