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


class DemRumNode(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "app_id": (str,),
            "id": (str,),
            "query": (str,),
        }

    attribute_map = {
        "app_id": "app_id",
        "id": "id",
        "query": "query",
    }

    def __init__(self_, query: str, app_id: Union[str, UnsetType] = unset, id: Union[str, UnsetType] = unset, **kwargs):
        """
        A RUM node within a journey step.

        :param app_id: The application ID associated with this node.
        :type app_id: str, optional

        :param id: The ID of the RUM node element.
        :type id: str, optional

        :param query: The RUM query for matching this node.
        :type query: str
        """
        if app_id is not unset:
            kwargs["app_id"] = app_id
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.query = query
