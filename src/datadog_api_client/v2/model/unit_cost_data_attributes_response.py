# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.unit_cost_query_definition import UnitCostQueryDefinition


class UnitCostDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.unit_cost_query_definition import UnitCostQueryDefinition

        return {
            "created_at": (datetime,),
            "created_by": (UUID,),
            "denominator_query": (UnitCostQueryDefinition,),
            "denominator_type": (str,),
            "description": (str, none_type),
            "name": (str,),
            "numerator_query": (UnitCostQueryDefinition,),
            "org_id": (int,),
            "unit_label": (str,),
            "updated_at": (datetime,),
            "updated_by": (UUID,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "denominator_query": "denominator_query",
        "denominator_type": "denominator_type",
        "description": "description",
        "name": "name",
        "numerator_query": "numerator_query",
        "org_id": "org_id",
        "unit_label": "unit_label",
        "updated_at": "updated_at",
        "updated_by": "updated_by",
    }

    def __init__(
        self_,
        created_at: datetime,
        created_by: UUID,
        denominator_query: UnitCostQueryDefinition,
        denominator_type: str,
        name: str,
        numerator_query: UnitCostQueryDefinition,
        org_id: int,
        unit_label: str,
        updated_at: datetime,
        updated_by: UUID,
        description: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a unit cost.

        :param created_at: The time the unit cost was created.
        :type created_at: datetime

        :param created_by: The UUID of the user who created the unit cost.
        :type created_by: UUID

        :param denominator_query: A timeseries object containing ``queries`` and ``formulas`` arrays.
        :type denominator_query: UnitCostQueryDefinition

        :param denominator_type: The data source of the denominator queries, or ``multisource`` when the denominator
            queries span more than one data source.
        :type denominator_type: str

        :param description: The description of the unit cost. Omitted when the unit cost has no description.
        :type description: str, none_type, optional

        :param name: The name of the unit cost.
        :type name: str

        :param numerator_query: A timeseries object containing ``queries`` and ``formulas`` arrays.
        :type numerator_query: UnitCostQueryDefinition

        :param org_id: The ID of the organization the unit cost belongs to.
        :type org_id: int

        :param unit_label: The label describing the denominator unit.
        :type unit_label: str

        :param updated_at: The time the unit cost was last updated.
        :type updated_at: datetime

        :param updated_by: The UUID of the user who last updated the unit cost.
        :type updated_by: UUID
        """
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.denominator_query = denominator_query
        self_.denominator_type = denominator_type
        self_.name = name
        self_.numerator_query = numerator_query
        self_.org_id = org_id
        self_.unit_label = unit_label
        self_.updated_at = updated_at
        self_.updated_by = updated_by
