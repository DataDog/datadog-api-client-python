# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_evsi_traffic_unavailable_reason import (
        ExperimentsEVSITrafficUnavailableReason,
    )


class ExperimentsEVSIContext(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_evsi_traffic_unavailable_reason import (
            ExperimentsEVSITrafficUnavailableReason,
        )

        return {
            "elapsed_days": (float, none_type),
            "horizon_days": (float,),
            "horizon_exposures": (float, none_type),
            "lookback_days": (int,),
            "lookback_exposures": (int, none_type),
            "total_exposures": (int, none_type),
            "unavailable_reason": (ExperimentsEVSITrafficUnavailableReason,),
            "usable_traffic_days": (int, none_type),
        }

    attribute_map = {
        "elapsed_days": "elapsed_days",
        "horizon_days": "horizon_days",
        "horizon_exposures": "horizon_exposures",
        "lookback_days": "lookback_days",
        "lookback_exposures": "lookback_exposures",
        "total_exposures": "total_exposures",
        "unavailable_reason": "unavailable_reason",
        "usable_traffic_days": "usable_traffic_days",
    }

    def __init__(
        self_,
        elapsed_days: Union[float, none_type],
        horizon_days: float,
        horizon_exposures: Union[float, none_type],
        lookback_days: int,
        lookback_exposures: Union[int, none_type],
        total_exposures: Union[int, none_type],
        unavailable_reason: Union[ExperimentsEVSITrafficUnavailableReason, none_type],
        usable_traffic_days: Union[int, none_type],
        **kwargs,
    ):
        """
        Forecast horizon and traffic counts used to calculate expected value of sample information (EVSI) for result_run_id. Assumes traffic continues at the rate observed during the lookback window. Omitted if the forecast was not recorded or could not be loaded.

        :param elapsed_days: Exact assignment-window duration in days, including fractional days.
        :type elapsed_days: float, none_type

        :param horizon_days: Forecast horizon in days from the original assignment window.
        :type horizon_days: float

        :param horizon_exposures: Projected additional exposures over the horizon, assuming constant traffic.
        :type horizon_exposures: float, none_type

        :param lookback_days: Selected lookback length in complete days.
        :type lookback_days: int

        :param lookback_exposures: Exposures across all variants in the eligible lookback buckets.
        :type lookback_exposures: int, none_type

        :param total_exposures: Experiment-wide exposures across the assignment window, including boundary buckets.
        :type total_exposures: int, none_type

        :param unavailable_reason: Recorded traffic forecast unavailability reason. Per-analysis reasons are reported separately.
        :type unavailable_reason: ExperimentsEVSITrafficUnavailableReason, none_type

        :param usable_traffic_days: Interior UTC daily buckets excluding both boundary days. Includes zero-traffic days and does not certify ingestion completeness.
        :type usable_traffic_days: int, none_type
        """
        super().__init__(kwargs)

        self_.elapsed_days = elapsed_days
        self_.horizon_days = horizon_days
        self_.horizon_exposures = horizon_exposures
        self_.lookback_days = lookback_days
        self_.lookback_exposures = lookback_exposures
        self_.total_exposures = total_exposures
        self_.unavailable_reason = unavailable_reason
        self_.usable_traffic_days = usable_traffic_days
