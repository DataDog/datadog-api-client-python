# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cost_anomaly import CostAnomaly


class CostAnomaliesResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_anomaly import CostAnomaly

        return {
            "anomalies": ([CostAnomaly],),
            "avg_daily_anomalous_cost": (float,),
            "total_actual_cost": (float,),
            "total_anomalous_cost": (float,),
            "total_count": (int,),
        }

    attribute_map = {
        "anomalies": "anomalies",
        "avg_daily_anomalous_cost": "avg_daily_anomalous_cost",
        "total_actual_cost": "total_actual_cost",
        "total_anomalous_cost": "total_anomalous_cost",
        "total_count": "total_count",
    }

    def __init__(
        self_,
        anomalies: List[CostAnomaly],
        avg_daily_anomalous_cost: float,
        total_actual_cost: float,
        total_anomalous_cost: float,
        total_count: int,
        **kwargs,
    ):
        """
        Cost anomaly results and aggregated totals for the queried window.

        :param anomalies: The list of cost anomalies that match the request.
        :type anomalies: [CostAnomaly]

        :param avg_daily_anomalous_cost: Average daily anomalous cost change across the queried window.
        :type avg_daily_anomalous_cost: float

        :param total_actual_cost: Total actual cost spent across the queried window for the matching providers.
        :type total_actual_cost: float

        :param total_anomalous_cost: Sum of the anomalous cost change across all returned anomalies.
        :type total_anomalous_cost: float

        :param total_count: Total number of anomalies that match the request.
        :type total_count: int
        """
        super().__init__(kwargs)

        self_.anomalies = anomalies
        self_.avg_daily_anomalous_cost = avg_daily_anomalous_cost
        self_.total_actual_cost = total_actual_cost
        self_.total_anomalous_cost = total_anomalous_cost
        self_.total_count = total_count
