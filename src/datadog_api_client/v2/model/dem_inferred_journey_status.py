# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DemInferredJourneyStatus(ModelSimple):
    """
    The status of an inferred DEM journey.

    :param value: If omitted defaults to "candidate". Must be one of ["candidate", "ignored"].
    :type value: str
    """

    allowed_values = {
        "candidate",
        "ignored",
    }
    CANDIDATE: ClassVar["DemInferredJourneyStatus"]
    IGNORED: ClassVar["DemInferredJourneyStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DemInferredJourneyStatus.CANDIDATE = DemInferredJourneyStatus("candidate")
DemInferredJourneyStatus.IGNORED = DemInferredJourneyStatus("ignored")
