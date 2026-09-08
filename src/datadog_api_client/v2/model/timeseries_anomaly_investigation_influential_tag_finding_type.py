# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TimeseriesAnomalyInvestigationInfluentialTagFindingType(ModelSimple):
    """
    Finding category for an influential tag.

    :param value: If omitted defaults to "influential_tag". Must be one of ["influential_tag"].
    :type value: str
    """

    allowed_values = {
        "influential_tag",
    }
    INFLUENTIAL_TAG: ClassVar["TimeseriesAnomalyInvestigationInfluentialTagFindingType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TimeseriesAnomalyInvestigationInfluentialTagFindingType.INFLUENTIAL_TAG = (
    TimeseriesAnomalyInvestigationInfluentialTagFindingType("influential_tag")
)
