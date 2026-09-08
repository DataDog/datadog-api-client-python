# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.unit_cost_query_definition import UnitCostQueryDefinition


class UnitCostRequestAttributes(ModelNormal):
    validations = {
        "description": {
            "max_length": 2000,
        },
        "name": {
            "max_length": 200,
        },
        "unit_label": {
            "max_length": 100,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.unit_cost_query_definition import UnitCostQueryDefinition

        return {
            "denominator_query": (UnitCostQueryDefinition,),
            "description": (str, none_type),
            "name": (str,),
            "numerator_query": (UnitCostQueryDefinition,),
            "unit_label": (str,),
        }

    attribute_map = {
        "denominator_query": "denominator_query",
        "description": "description",
        "name": "name",
        "numerator_query": "numerator_query",
        "unit_label": "unit_label",
    }

    def __init__(
        self_,
        denominator_query: UnitCostQueryDefinition,
        name: str,
        numerator_query: UnitCostQueryDefinition,
        unit_label: str,
        description: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a unit cost create or replace request.

        :param denominator_query: A timeseries object containing ``queries`` and ``formulas`` arrays.
        :type denominator_query: UnitCostQueryDefinition

        :param description: An optional description of the unit cost. At most 2000 characters.
        :type description: str, none_type, optional

        :param name: The name of the unit cost. At most 200 characters.
        :type name: str

        :param numerator_query: A timeseries object containing ``queries`` and ``formulas`` arrays.
        :type numerator_query: UnitCostQueryDefinition

        :param unit_label: The label describing the denominator unit, for example ``user``. At most 100 characters.
        :type unit_label: str
        """
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.denominator_query = denominator_query
        self_.name = name
        self_.numerator_query = numerator_query
        self_.unit_label = unit_label
