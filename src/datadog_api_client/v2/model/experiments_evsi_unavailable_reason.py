# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsEVSIUnavailableReason(ModelSimple):
    """
    Recorded reason this analysis has no EVSI estimate. Omitted when unrecorded; absence does not establish availability for historical or imported results. Controls and non-Bayesian analyses omit this field.

    :param value: Must be one of ["traffic_unavailable", "insufficient_complete_days", "no_total_exposures", "no_lookback_exposures", "invalid_traffic", "invalid_standard_error", "computation_failed", "analysis_unavailable"].
    :type value: str
    """

    allowed_values = {
        "traffic_unavailable",
        "insufficient_complete_days",
        "no_total_exposures",
        "no_lookback_exposures",
        "invalid_traffic",
        "invalid_standard_error",
        "computation_failed",
        "analysis_unavailable",
    }
    TRAFFIC_UNAVAILABLE: ClassVar["ExperimentsEVSIUnavailableReason"]
    INSUFFICIENT_COMPLETE_DAYS: ClassVar["ExperimentsEVSIUnavailableReason"]
    NO_TOTAL_EXPOSURES: ClassVar["ExperimentsEVSIUnavailableReason"]
    NO_LOOKBACK_EXPOSURES: ClassVar["ExperimentsEVSIUnavailableReason"]
    INVALID_TRAFFIC: ClassVar["ExperimentsEVSIUnavailableReason"]
    INVALID_STANDARD_ERROR: ClassVar["ExperimentsEVSIUnavailableReason"]
    COMPUTATION_FAILED: ClassVar["ExperimentsEVSIUnavailableReason"]
    ANALYSIS_UNAVAILABLE: ClassVar["ExperimentsEVSIUnavailableReason"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsEVSIUnavailableReason.TRAFFIC_UNAVAILABLE = ExperimentsEVSIUnavailableReason("traffic_unavailable")
ExperimentsEVSIUnavailableReason.INSUFFICIENT_COMPLETE_DAYS = ExperimentsEVSIUnavailableReason(
    "insufficient_complete_days"
)
ExperimentsEVSIUnavailableReason.NO_TOTAL_EXPOSURES = ExperimentsEVSIUnavailableReason("no_total_exposures")
ExperimentsEVSIUnavailableReason.NO_LOOKBACK_EXPOSURES = ExperimentsEVSIUnavailableReason("no_lookback_exposures")
ExperimentsEVSIUnavailableReason.INVALID_TRAFFIC = ExperimentsEVSIUnavailableReason("invalid_traffic")
ExperimentsEVSIUnavailableReason.INVALID_STANDARD_ERROR = ExperimentsEVSIUnavailableReason("invalid_standard_error")
ExperimentsEVSIUnavailableReason.COMPUTATION_FAILED = ExperimentsEVSIUnavailableReason("computation_failed")
ExperimentsEVSIUnavailableReason.ANALYSIS_UNAVAILABLE = ExperimentsEVSIUnavailableReason("analysis_unavailable")
