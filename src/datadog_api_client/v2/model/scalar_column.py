# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.unit import Unit


class ScalarColumn(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.unit import Unit

        return {
            "unit": ([Unit, none_type],),
            "values": ([float],),
        }

    attribute_map = {
        "unit": "unit",
        "values": "values",
    }

    def __init__(
        self_, unit: Union[List[Unit], UnsetType] = unset, values: Union[List[float], UnsetType] = unset, **kwargs
    ):
        """
        A single column in a scalar query response.

        :param unit: List of units.
        :type unit: [Unit, none_type], optional

        :param values: Array of values for each group-by combination that results from one formula or query.
        :type values: [float], optional
        """
        if unit is not unset:
            kwargs["unit"] = unit
        if values is not unset:
            kwargs["values"] = values
        super().__init__(kwargs)
