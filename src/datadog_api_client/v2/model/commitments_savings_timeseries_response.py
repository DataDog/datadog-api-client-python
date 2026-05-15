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
    from datadog_api_client.v2.model.commitments_timeseries_metric import CommitmentsTimeseriesMetric


class CommitmentsSavingsTimeseriesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_timeseries_metric import CommitmentsTimeseriesMetric

        return {
            "actual_cost": (CommitmentsTimeseriesMetric,),
            "effective_savings_rate": (CommitmentsTimeseriesMetric,),
            "on_demand_equivalent_cost": (CommitmentsTimeseriesMetric,),
            "realized_savings": (CommitmentsTimeseriesMetric,),
        }

    attribute_map = {
        "actual_cost": "actual_cost",
        "effective_savings_rate": "effective_savings_rate",
        "on_demand_equivalent_cost": "on_demand_equivalent_cost",
        "realized_savings": "realized_savings",
    }

    def __init__(
        self_,
        actual_cost: CommitmentsTimeseriesMetric,
        effective_savings_rate: CommitmentsTimeseriesMetric,
        on_demand_equivalent_cost: CommitmentsTimeseriesMetric,
        realized_savings: CommitmentsTimeseriesMetric,
        **kwargs,
    ):
        """
        Response containing timeseries savings metrics for cloud commitment programs.

        :param actual_cost: A timeseries metric containing timestamps, series values, and optional unit metadata.
        :type actual_cost: CommitmentsTimeseriesMetric

        :param effective_savings_rate: A timeseries metric containing timestamps, series values, and optional unit metadata.
        :type effective_savings_rate: CommitmentsTimeseriesMetric

        :param on_demand_equivalent_cost: A timeseries metric containing timestamps, series values, and optional unit metadata.
        :type on_demand_equivalent_cost: CommitmentsTimeseriesMetric

        :param realized_savings: A timeseries metric containing timestamps, series values, and optional unit metadata.
        :type realized_savings: CommitmentsTimeseriesMetric
        """
        super().__init__(kwargs)

        self_.actual_cost = actual_cost
        self_.effective_savings_rate = effective_savings_rate
        self_.on_demand_equivalent_cost = on_demand_equivalent_cost
        self_.realized_savings = realized_savings
