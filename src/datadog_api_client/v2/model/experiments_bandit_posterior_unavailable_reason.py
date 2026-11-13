# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsBanditPosteriorUnavailableReason(ModelSimple):
    """
    Why the arm's estimate and interval are unavailable. Absent when they are available.

    :param value: Must be one of ["no_data", "insufficient_data", "zero_variance"].
    :type value: str
    """

    allowed_values = {
        "no_data",
        "insufficient_data",
        "zero_variance",
    }
    NO_DATA: ClassVar["ExperimentsBanditPosteriorUnavailableReason"]
    INSUFFICIENT_DATA: ClassVar["ExperimentsBanditPosteriorUnavailableReason"]
    ZERO_VARIANCE: ClassVar["ExperimentsBanditPosteriorUnavailableReason"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsBanditPosteriorUnavailableReason.NO_DATA = ExperimentsBanditPosteriorUnavailableReason("no_data")
ExperimentsBanditPosteriorUnavailableReason.INSUFFICIENT_DATA = ExperimentsBanditPosteriorUnavailableReason(
    "insufficient_data"
)
ExperimentsBanditPosteriorUnavailableReason.ZERO_VARIANCE = ExperimentsBanditPosteriorUnavailableReason("zero_variance")
