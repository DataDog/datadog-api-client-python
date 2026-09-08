# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TimeseriesAnomalyInvestigationMetaType(ModelSimple):
    """
    Response metadata type for a timeseries anomaly investigation.

    :param value: If omitted defaults to "timeseries_anomaly_investigation". Must be one of ["timeseries_anomaly_investigation"].
    :type value: str
    """

    allowed_values = {
        "timeseries_anomaly_investigation",
    }
    TIMESERIES_ANOMALY_INVESTIGATION: ClassVar["TimeseriesAnomalyInvestigationMetaType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TimeseriesAnomalyInvestigationMetaType.TIMESERIES_ANOMALY_INVESTIGATION = TimeseriesAnomalyInvestigationMetaType(
    "timeseries_anomaly_investigation"
)
