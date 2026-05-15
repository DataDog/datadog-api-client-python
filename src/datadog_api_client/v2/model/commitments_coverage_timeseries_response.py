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


class CommitmentsCoverageTimeseriesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_timeseries_metric import CommitmentsTimeseriesMetric

        return {
            "cost": (CommitmentsTimeseriesMetric,),
            "hours": (CommitmentsTimeseriesMetric,),
        }

    attribute_map = {
        "cost": "cost",
        "hours": "hours",
    }

    def __init__(self_, cost: CommitmentsTimeseriesMetric, hours: CommitmentsTimeseriesMetric, **kwargs):
        """
        Response containing timeseries coverage metrics for cloud commitment programs.

        :param cost: A timeseries metric containing timestamps, series values, and optional unit metadata.
        :type cost: CommitmentsTimeseriesMetric

        :param hours: A timeseries metric containing timestamps, series values, and optional unit metadata.
        :type hours: CommitmentsTimeseriesMetric
        """
        super().__init__(kwargs)

        self_.cost = cost
        self_.hours = hours
