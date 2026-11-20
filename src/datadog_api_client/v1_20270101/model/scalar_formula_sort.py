# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.scalar_formula_order_by import ScalarFormulaOrderBy
    from datadog_api_client.v1_20270101.model.formula_order_by_group import FormulaOrderByGroup
    from datadog_api_client.v1_20270101.model.formula_order_by_formula_index import FormulaOrderByFormulaIndex


class ScalarFormulaSort(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.scalar_formula_order_by import ScalarFormulaOrderBy

        return {
            "count": (float,),
            "offset": (float,),
            "order_by": ([ScalarFormulaOrderBy],),
        }

    attribute_map = {
        "count": "count",
        "offset": "offset",
        "order_by": "order_by",
    }

    def __init__(
        self_,
        count: Union[float, UnsetType] = unset,
        offset: Union[float, UnsetType] = unset,
        order_by: Union[
            List[Union[ScalarFormulaOrderBy, FormulaOrderByGroup, FormulaOrderByFormulaIndex]], UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param count: Test-only generated schema for the dashboard versioning proof of concept.
        :type count: float, optional

        :param offset: Test-only generated schema for the dashboard versioning proof of concept.
        :type offset: float, optional

        :param order_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type order_by: [ScalarFormulaOrderBy], optional
        """
        if count is not unset:
            kwargs["count"] = count
        if offset is not unset:
            kwargs["offset"] = offset
        if order_by is not unset:
            kwargs["order_by"] = order_by
        super().__init__(kwargs)
