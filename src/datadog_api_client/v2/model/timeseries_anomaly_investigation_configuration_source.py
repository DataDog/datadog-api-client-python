# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TimeseriesAnomalyInvestigationConfigurationSource(ModelSimple):
    """
    Source of the anomaly detection configuration.

    :param value: Must be one of ["request_formula", "watchdog_explains_default"].
    :type value: str
    """

    allowed_values = {
        "request_formula",
        "watchdog_explains_default",
    }
    REQUEST_FORMULA: ClassVar["TimeseriesAnomalyInvestigationConfigurationSource"]
    WATCHDOG_EXPLAINS_DEFAULT: ClassVar["TimeseriesAnomalyInvestigationConfigurationSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TimeseriesAnomalyInvestigationConfigurationSource.REQUEST_FORMULA = TimeseriesAnomalyInvestigationConfigurationSource(
    "request_formula"
)
TimeseriesAnomalyInvestigationConfigurationSource.WATCHDOG_EXPLAINS_DEFAULT = (
    TimeseriesAnomalyInvestigationConfigurationSource("watchdog_explains_default")
)
