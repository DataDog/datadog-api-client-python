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


class ExperimentsMetricV2DTODataAttributesPercentileAggregationWarehouseMetricMeasure(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "pipeline_column_suffix": (str,),
        }

    attribute_map = {
        "id": "id",
        "pipeline_column_suffix": "pipeline_column_suffix",
    }

    def __init__(
        self_, id: Union[str, UnsetType] = unset, pipeline_column_suffix: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Warehouse measure that supplies values for the metric.

        :param id: ID of the measure.
        :type id: str, optional

        :param pipeline_column_suffix: Suffix used to identify this value in pipeline output columns.
        :type pipeline_column_suffix: str, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if pipeline_column_suffix is not unset:
            kwargs["pipeline_column_suffix"] = pipeline_column_suffix
        super().__init__(kwargs)
