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
    from datadog_api_client.v2.model.model_lab_metric_stat_range import ModelLabMetricStatRange
    from datadog_api_client.v2.model.model_lab_numeric_range import ModelLabNumericRange


class ModelLabFacetValuesAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.model_lab_metric_stat_range import ModelLabMetricStatRange
        from datadog_api_client.v2.model.model_lab_numeric_range import ModelLabNumericRange

        return {
            "facet_name": (str,),
            "facet_type": (str,),
            "metric_stat_ranges": ([ModelLabMetricStatRange],),
            "numeric_range": (ModelLabNumericRange,),
            "values": ([str],),
        }

    attribute_map = {
        "facet_name": "facet_name",
        "facet_type": "facet_type",
        "metric_stat_ranges": "metric_stat_ranges",
        "numeric_range": "numeric_range",
        "values": "values",
    }

    def __init__(
        self_,
        facet_name: str,
        facet_type: str,
        values: List[str],
        metric_stat_ranges: Union[List[ModelLabMetricStatRange], UnsetType] = unset,
        numeric_range: Union[ModelLabNumericRange, UnsetType] = unset,
        **kwargs,
    ):
        """
        Available values for a specific facet key.

        :param facet_name: The name of the facet.
        :type facet_name: str

        :param facet_type: The type of the facet.
        :type facet_type: str

        :param metric_stat_ranges: The ranges for each metric statistic.
        :type metric_stat_ranges: [ModelLabMetricStatRange], optional

        :param numeric_range: The numeric range of values for a facet.
        :type numeric_range: ModelLabNumericRange, optional

        :param values: The list of available string values for this facet.
        :type values: [str]
        """
        if metric_stat_ranges is not unset:
            kwargs["metric_stat_ranges"] = metric_stat_ranges
        if numeric_range is not unset:
            kwargs["numeric_range"] = numeric_range
        super().__init__(kwargs)

        self_.facet_name = facet_name
        self_.facet_type = facet_type
        self_.values = values
