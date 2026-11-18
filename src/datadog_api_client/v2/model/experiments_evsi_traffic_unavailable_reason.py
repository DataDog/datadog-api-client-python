# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsEVSITrafficUnavailableReason(ModelSimple):
    """
    Recorded traffic forecast unavailability reason. Per-analysis reasons are reported separately.

    :param value: Must be one of ["traffic_unavailable", "insufficient_complete_days", "no_total_exposures", "no_lookback_exposures", "invalid_traffic"].
    :type value: str
    """

    allowed_values = {
        "traffic_unavailable",
        "insufficient_complete_days",
        "no_total_exposures",
        "no_lookback_exposures",
        "invalid_traffic",
    }
    TRAFFIC_UNAVAILABLE: ClassVar["ExperimentsEVSITrafficUnavailableReason"]
    INSUFFICIENT_COMPLETE_DAYS: ClassVar["ExperimentsEVSITrafficUnavailableReason"]
    NO_TOTAL_EXPOSURES: ClassVar["ExperimentsEVSITrafficUnavailableReason"]
    NO_LOOKBACK_EXPOSURES: ClassVar["ExperimentsEVSITrafficUnavailableReason"]
    INVALID_TRAFFIC: ClassVar["ExperimentsEVSITrafficUnavailableReason"]

    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsEVSITrafficUnavailableReason.TRAFFIC_UNAVAILABLE = ExperimentsEVSITrafficUnavailableReason(
    "traffic_unavailable"
)
ExperimentsEVSITrafficUnavailableReason.INSUFFICIENT_COMPLETE_DAYS = ExperimentsEVSITrafficUnavailableReason(
    "insufficient_complete_days"
)
ExperimentsEVSITrafficUnavailableReason.NO_TOTAL_EXPOSURES = ExperimentsEVSITrafficUnavailableReason(
    "no_total_exposures"
)
ExperimentsEVSITrafficUnavailableReason.NO_LOOKBACK_EXPOSURES = ExperimentsEVSITrafficUnavailableReason(
    "no_lookback_exposures"
)
ExperimentsEVSITrafficUnavailableReason.INVALID_TRAFFIC = ExperimentsEVSITrafficUnavailableReason("invalid_traffic")
