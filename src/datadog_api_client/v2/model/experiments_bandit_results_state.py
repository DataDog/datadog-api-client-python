# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsBanditResultsState(ModelSimple):
    """
    WAITING_FOR_FIRST_REFRESH until a refresh saves results. STATS_UNAVAILABLE when the latest saved refresh has no complete probabilities of being optimal. ENDED once the bandit is stopped or completed; its last estimates stay. Otherwise WARMUP or OPTIMIZING says which policy the bandit serves. A paused bandit keeps its state.

    :param value: Must be one of ["WAITING_FOR_FIRST_REFRESH", "WARMUP", "OPTIMIZING", "STATS_UNAVAILABLE", "ENDED"].
    :type value: str
    """

    allowed_values = {
        "WAITING_FOR_FIRST_REFRESH",
        "WARMUP",
        "OPTIMIZING",
        "STATS_UNAVAILABLE",
        "ENDED",
    }
    WAITING_FOR_FIRST_REFRESH: ClassVar["ExperimentsBanditResultsState"]
    WARMUP: ClassVar["ExperimentsBanditResultsState"]
    OPTIMIZING: ClassVar["ExperimentsBanditResultsState"]
    STATS_UNAVAILABLE: ClassVar["ExperimentsBanditResultsState"]
    ENDED: ClassVar["ExperimentsBanditResultsState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsBanditResultsState.WAITING_FOR_FIRST_REFRESH = ExperimentsBanditResultsState("WAITING_FOR_FIRST_REFRESH")
ExperimentsBanditResultsState.WARMUP = ExperimentsBanditResultsState("WARMUP")
ExperimentsBanditResultsState.OPTIMIZING = ExperimentsBanditResultsState("OPTIMIZING")
ExperimentsBanditResultsState.STATS_UNAVAILABLE = ExperimentsBanditResultsState("STATS_UNAVAILABLE")
ExperimentsBanditResultsState.ENDED = ExperimentsBanditResultsState("ENDED")
