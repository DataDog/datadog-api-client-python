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
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_anomaly import (
        TimeseriesAnomalyInvestigationAnomaly,
    )
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_complete_status import (
        TimeseriesAnomalyInvestigationCompleteStatus,
    )


class TimeseriesAnomalyInvestigationResult(ModelNormal):
    validations = {
        "anomalies": {
            "max_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_anomaly import (
            TimeseriesAnomalyInvestigationAnomaly,
        )
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_complete_status import (
            TimeseriesAnomalyInvestigationCompleteStatus,
        )

        return {
            "anomalies": ([TimeseriesAnomalyInvestigationAnomaly],),
            "status": (TimeseriesAnomalyInvestigationCompleteStatus,),
        }

    attribute_map = {
        "anomalies": "anomalies",
        "status": "status",
    }

    def __init__(
        self_,
        anomalies: List[TimeseriesAnomalyInvestigationAnomaly],
        status: TimeseriesAnomalyInvestigationCompleteStatus,
        **kwargs,
    ):
        """
        Completed result for one timeseries request. The anomalies array is empty when no qualifying anomaly is found.

        :param anomalies: Detected anomalies. This API version returns at most one anomaly.
        :type anomalies: [TimeseriesAnomalyInvestigationAnomaly]

        :param status: Status value indicating successful completion.
        :type status: TimeseriesAnomalyInvestigationCompleteStatus
        """
        super().__init__(kwargs)

        self_.anomalies = anomalies
        self_.status = status
