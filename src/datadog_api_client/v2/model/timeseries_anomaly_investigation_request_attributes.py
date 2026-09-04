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
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_timeseries_request import (
        TimeseriesAnomalyInvestigationTimeseriesRequest,
    )


class TimeseriesAnomalyInvestigationRequestAttributes(ModelNormal):
    validations = {
        "requests": {
            "max_items": 1,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_timeseries_request import (
            TimeseriesAnomalyInvestigationTimeseriesRequest,
        )

        return {
            "requests": ([TimeseriesAnomalyInvestigationTimeseriesRequest],),
        }

    attribute_map = {
        "requests": "requests",
    }

    def __init__(self_, requests: List[TimeseriesAnomalyInvestigationTimeseriesRequest], **kwargs):
        """
        Attributes of an anomaly investigation request.

        :param requests: Timeseries requests to investigate. This API version accepts exactly one request.
        :type requests: [TimeseriesAnomalyInvestigationTimeseriesRequest]
        """
        super().__init__(kwargs)

        self_.requests = requests
