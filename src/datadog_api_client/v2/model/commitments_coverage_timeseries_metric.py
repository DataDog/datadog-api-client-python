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
    from datadog_api_client.v2.model.commitments_provider import CommitmentsProvider
    from datadog_api_client.v2.model.commitments_timeseries_series import CommitmentsTimeseriesSeries
    from datadog_api_client.v2.model.commitments_unit import CommitmentsUnit


class CommitmentsCoverageTimeseriesMetric(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_provider import CommitmentsProvider
        from datadog_api_client.v2.model.commitments_timeseries_series import CommitmentsTimeseriesSeries
        from datadog_api_client.v2.model.commitments_unit import CommitmentsUnit

        return {
            "provider": (CommitmentsProvider,),
            "series": (CommitmentsTimeseriesSeries,),
            "times": ([int],),
            "unit": (CommitmentsUnit,),
        }

    attribute_map = {
        "provider": "provider",
        "series": "series",
        "times": "times",
        "unit": "unit",
    }

    def __init__(
        self_,
        provider: CommitmentsProvider,
        series: CommitmentsTimeseriesSeries,
        times: List[int],
        unit: Union[CommitmentsUnit, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        A coverage timeseries metric. For AWS and Azure, ``series`` holds the ``on_demand_only`` , ``spot_only`` , ``ri`` ,
        and ``sp`` buckets, plus ``ppp`` for Azure pre-purchase plans when enabled. For GCP, ``series`` holds the
        ``on_demand_only`` and ``flex_cud`` buckets.

        :param provider: Cloud provider for commitment programs.
        :type provider: CommitmentsProvider

        :param series: Timeseries data as a map of series names to their corresponding value arrays.
        :type series: CommitmentsTimeseriesSeries

        :param times: Unix timestamps in seconds for the timeseries data points.
        :type times: [int]

        :param unit: Unit metadata for a numeric metric. Unset fields are omitted, and the unit is ``null`` when it is unknown.
        :type unit: CommitmentsUnit, none_type, optional
        """
        if unit is not unset:
            kwargs["unit"] = unit
        super().__init__(kwargs)

        self_.provider = provider
        self_.series = series
        self_.times = times
