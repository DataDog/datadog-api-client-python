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
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_result import TimeseriesAnomalyInvestigationResult


class TimeseriesAnomalyInvestigationResponseAttributes(ModelNormal):
    validations = {
        "results": {
            "max_items": 1,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_result import (
            TimeseriesAnomalyInvestigationResult,
        )

        return {
            "results": ([TimeseriesAnomalyInvestigationResult],),
        }

    attribute_map = {
        "results": "results",
    }

    def __init__(self_, results: List[TimeseriesAnomalyInvestigationResult], **kwargs):
        """
        Attributes of an anomaly investigation response.

        :param results: Results returned in the same order as the submitted requests. This API version returns exactly one result.
        :type results: [TimeseriesAnomalyInvestigationResult]
        """
        super().__init__(kwargs)

        self_.results = results
