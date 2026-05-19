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


class RecommendationsFilterRequestSortItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "expression": (str,),
            "order": (str,),
        }

    attribute_map = {
        "expression": "expression",
        "order": "order",
    }

    def __init__(self_, expression: Union[str, UnsetType] = unset, order: Union[str, UnsetType] = unset, **kwargs):
        """
        A single sort clause applied to the cost recommendations result set.

        :param expression: Field to sort by (for example, ``potential_daily_savings.amount`` ).
        :type expression: str, optional

        :param order: Sort direction, either ``ASC`` or ``DESC``.
        :type order: str, optional
        """
        if expression is not unset:
            kwargs["expression"] = expression
        if order is not unset:
            kwargs["order"] = order
        super().__init__(kwargs)
