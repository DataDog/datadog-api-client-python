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
    from datadog_api_client.v2.model.commitments_unused_cost_meta import CommitmentsUnusedCostMeta
    from datadog_api_client.v2.model.commitments_query_definition import CommitmentsQueryDefinition
    from datadog_api_client.v2.model.commitments_timeseries_series import CommitmentsTimeseriesSeries
    from datadog_api_client.v2.model.commitments_unit import CommitmentsUnit


class CommitmentsUtilizationTimeseriesResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_unused_cost_meta import CommitmentsUnusedCostMeta
        from datadog_api_client.v2.model.commitments_query_definition import CommitmentsQueryDefinition
        from datadog_api_client.v2.model.commitments_timeseries_series import CommitmentsTimeseriesSeries
        from datadog_api_client.v2.model.commitments_unit import CommitmentsUnit

        return {
            "meta": (CommitmentsUnusedCostMeta,),
            "query_definition": (CommitmentsQueryDefinition,),
            "series": (CommitmentsTimeseriesSeries,),
            "times": ([int],),
            "unit": (CommitmentsUnit,),
        }

    attribute_map = {
        "meta": "meta",
        "query_definition": "query_definition",
        "series": "series",
        "times": "times",
        "unit": "unit",
    }

    def __init__(
        self_,
        series: CommitmentsTimeseriesSeries,
        times: List[int],
        meta: Union[CommitmentsUnusedCostMeta, UnsetType] = unset,
        query_definition: Union[CommitmentsQueryDefinition, UnsetType] = unset,
        unit: Union[CommitmentsUnit, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a timeseries utilization response.

        :param meta: Metadata reporting that the cost data lacks the unused costs of some commitments, as with Azure exports
            scoped below the billing profile. Utilization is then overstated, and realized savings and effective
            savings rate are upper bounds. Omitted when the unused costs are available.
        :type meta: CommitmentsUnusedCostMeta, optional

        :param query_definition: The query that produces the response values, in the same format as dashboard and notebook widget
            requests, so a client can graph the values in a widget. Each formula's ``id`` names the response value
            that it produces.
        :type query_definition: CommitmentsQueryDefinition, optional

        :param series: Timeseries data as a map of series names to their corresponding value arrays.
        :type series: CommitmentsTimeseriesSeries

        :param times: Unix timestamps in seconds for the timeseries data points.
        :type times: [int]

        :param unit: Unit metadata for a numeric metric. Unset fields are omitted, and the unit is ``null`` when it is unknown.
        :type unit: CommitmentsUnit, none_type, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        if query_definition is not unset:
            kwargs["query_definition"] = query_definition
        if unit is not unset:
            kwargs["unit"] = unit
        super().__init__(kwargs)

        self_.series = series
        self_.times = times
