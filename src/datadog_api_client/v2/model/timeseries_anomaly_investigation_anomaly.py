# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_detection import (
        TimeseriesAnomalyInvestigationDetection,
    )
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_interval import (
        TimeseriesAnomalyInvestigationInterval,
    )
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_finding import (
        TimeseriesAnomalyInvestigationFinding,
    )
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_maximum_deviation import (
        TimeseriesAnomalyInvestigationMaximumDeviation,
    )
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_series import TimeseriesAnomalyInvestigationSeries
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_tag_analysis import (
        TimeseriesAnomalyInvestigationTagAnalysis,
    )
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_anomaly_type import (
        TimeseriesAnomalyInvestigationAnomalyType,
    )
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_influential_tag_finding import (
        TimeseriesAnomalyInvestigationInfluentialTagFinding,
    )
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_anomaly_finding import (
        TimeseriesAnomalyInvestigationAnomalyFinding,
    )


class TimeseriesAnomalyInvestigationAnomaly(ModelNormal):
    validations = {
        "findings": {
            "max_items": 3,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_detection import (
            TimeseriesAnomalyInvestigationDetection,
        )
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_interval import (
            TimeseriesAnomalyInvestigationInterval,
        )
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_finding import (
            TimeseriesAnomalyInvestigationFinding,
        )
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_maximum_deviation import (
            TimeseriesAnomalyInvestigationMaximumDeviation,
        )
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_series import (
            TimeseriesAnomalyInvestigationSeries,
        )
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_tag_analysis import (
            TimeseriesAnomalyInvestigationTagAnalysis,
        )
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_anomaly_type import (
            TimeseriesAnomalyInvestigationAnomalyType,
        )

        return {
            "anomaly_detection": (TimeseriesAnomalyInvestigationDetection,),
            "detected_interval": (TimeseriesAnomalyInvestigationInterval,),
            "display_interval": (TimeseriesAnomalyInvestigationInterval,),
            "findings": ([TimeseriesAnomalyInvestigationFinding],),
            "maximum_deviation": (TimeseriesAnomalyInvestigationMaximumDeviation,),
            "series": (TimeseriesAnomalyInvestigationSeries,),
            "tag_analysis": (TimeseriesAnomalyInvestigationTagAnalysis,),
            "type": (TimeseriesAnomalyInvestigationAnomalyType,),
        }

    attribute_map = {
        "anomaly_detection": "anomaly_detection",
        "detected_interval": "detected_interval",
        "display_interval": "display_interval",
        "findings": "findings",
        "maximum_deviation": "maximum_deviation",
        "series": "series",
        "tag_analysis": "tag_analysis",
        "type": "type",
    }

    def __init__(
        self_,
        anomaly_detection: TimeseriesAnomalyInvestigationDetection,
        detected_interval: TimeseriesAnomalyInvestigationInterval,
        display_interval: TimeseriesAnomalyInvestigationInterval,
        findings: List[
            Union[
                TimeseriesAnomalyInvestigationFinding,
                TimeseriesAnomalyInvestigationInfluentialTagFinding,
                TimeseriesAnomalyInvestigationAnomalyFinding,
            ]
        ],
        maximum_deviation: TimeseriesAnomalyInvestigationMaximumDeviation,
        series: TimeseriesAnomalyInvestigationSeries,
        tag_analysis: TimeseriesAnomalyInvestigationTagAnalysis,
        type: TimeseriesAnomalyInvestigationAnomalyType,
        **kwargs,
    ):
        """
        Most significant anomaly detected in the request.

        :param anomaly_detection: Anomaly detection configuration used for the result.
        :type anomaly_detection: TimeseriesAnomalyInvestigationDetection

        :param detected_interval: Half-open time interval in milliseconds since the Unix epoch.
        :type detected_interval: TimeseriesAnomalyInvestigationInterval

        :param display_interval: Half-open time interval in milliseconds since the Unix epoch.
        :type display_interval: TimeseriesAnomalyInvestigationInterval

        :param findings: Deterministic explanations for the anomaly, ordered by importance.
        :type findings: [TimeseriesAnomalyInvestigationFinding]

        :param maximum_deviation: Most anomalous point within the detected interval.
        :type maximum_deviation: TimeseriesAnomalyInvestigationMaximumDeviation

        :param series: Logical series on which the anomaly was detected.
        :type series: TimeseriesAnomalyInvestigationSeries

        :param tag_analysis: Summary of optional influential-tag enrichment. Count and key fields are present only when analysis completes; enrichment availability does not affect completion of the investigation result.
        :type tag_analysis: TimeseriesAnomalyInvestigationTagAnalysis

        :param type: Direction of an anomaly relative to its expected range.
        :type type: TimeseriesAnomalyInvestigationAnomalyType
        """
        super().__init__(kwargs)

        self_.anomaly_detection = anomaly_detection
        self_.detected_interval = detected_interval
        self_.display_interval = display_interval
        self_.findings = findings
        self_.maximum_deviation = maximum_deviation
        self_.series = series
        self_.tag_analysis = tag_analysis
        self_.type = type
