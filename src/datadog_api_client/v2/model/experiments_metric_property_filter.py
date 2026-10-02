# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ExperimentsMetricPropertyFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "measure_id": (str,),
            "operation": (str,),
            "property_id": (str,),
            "values": ([str],),
        }

    attribute_map = {
        "measure_id": "measure_id",
        "operation": "operation",
        "property_id": "property_id",
        "values": "values",
    }

    def __init__(
        self_,
        measure_id: Union[str, UnsetType] = unset,
        operation: Union[str, UnsetType] = unset,
        property_id: Union[str, UnsetType] = unset,
        values: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        A comparison that selects metric data by a property or measure.

        :param measure_id: ID of the measure evaluated by the filter.
        :type measure_id: str, optional

        :param operation: Comparison applied by the filter.
        :type operation: str, optional

        :param property_id: ID of the property evaluated by the filter.
        :type property_id: str, optional

        :param values: Values used by the filter's comparison.
        :type values: [str], optional
        """
        if measure_id is not unset:
            kwargs["measure_id"] = measure_id
        if operation is not unset:
            kwargs["operation"] = operation
        if property_id is not unset:
            kwargs["property_id"] = property_id
        if values is not unset:
            kwargs["values"] = values
        super().__init__(kwargs)
