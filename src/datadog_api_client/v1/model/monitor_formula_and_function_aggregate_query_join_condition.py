# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_query_join_type import (
        MonitorFormulaAndFunctionAggregateQueryJoinType,
    )


class MonitorFormulaAndFunctionAggregateQueryJoinCondition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_formula_and_function_aggregate_query_join_type import (
            MonitorFormulaAndFunctionAggregateQueryJoinType,
        )

        return {
            "augment_attribute": (str,),
            "base_attribute": (str,),
            "join_type": (MonitorFormulaAndFunctionAggregateQueryJoinType,),
        }

    attribute_map = {
        "augment_attribute": "augment_attribute",
        "base_attribute": "base_attribute",
        "join_type": "join_type",
    }

    def __init__(
        self_,
        augment_attribute: str,
        base_attribute: str,
        join_type: MonitorFormulaAndFunctionAggregateQueryJoinType,
        **kwargs,
    ):
        """
        Join condition for aggregate augmented queries.

        :param augment_attribute: Attribute from the augment query to join on.
        :type augment_attribute: str

        :param base_attribute: Attribute from the base query to join on.
        :type base_attribute: str

        :param join_type: Join type for aggregate query join conditions.
        :type join_type: MonitorFormulaAndFunctionAggregateQueryJoinType
        """
        super().__init__(kwargs)

        self_.augment_attribute = augment_attribute
        self_.base_attribute = base_attribute
        self_.join_type = join_type
