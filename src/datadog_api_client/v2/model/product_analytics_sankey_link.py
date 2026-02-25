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


class ProductAnalyticsSankeyLink(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "column": (int,),
            "id": (str,),
            "source": (str,),
            "target": (str,),
            "value": (int,),
        }

    attribute_map = {
        "column": "column",
        "id": "id",
        "source": "source",
        "target": "target",
        "value": "value",
    }

    def __init__(
        self_,
        column: Union[int, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        source: Union[str, UnsetType] = unset,
        target: Union[str, UnsetType] = unset,
        value: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        A link between two nodes in the Sankey diagram.

        :param column: The step column of the source node.
        :type column: int, optional

        :param id:
        :type id: str, optional

        :param source: The source node ID.
        :type source: str, optional

        :param target: The target node ID.
        :type target: str, optional

        :param value: The number of sessions through this link.
        :type value: int, optional
        """
        if column is not unset:
            kwargs["column"] = column
        if id is not unset:
            kwargs["id"] = id
        if source is not unset:
            kwargs["source"] = source
        if target is not unset:
            kwargs["target"] = target
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
