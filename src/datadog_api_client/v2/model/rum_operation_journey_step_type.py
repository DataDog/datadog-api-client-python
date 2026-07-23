# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RUMOperationJourneyStepType(ModelSimple):
    """
    The type of a step within a RUM operation's journey.

    :param value: Must be one of ["start", "update", "stop", "error", "abandoned"].
    :type value: str
    """

    allowed_values = {
        "start",
        "update",
        "stop",
        "error",
        "abandoned",
    }
    START: ClassVar["RUMOperationJourneyStepType"]
    UPDATE: ClassVar["RUMOperationJourneyStepType"]
    STOP: ClassVar["RUMOperationJourneyStepType"]
    ERROR: ClassVar["RUMOperationJourneyStepType"]
    ABANDONED: ClassVar["RUMOperationJourneyStepType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RUMOperationJourneyStepType.START = RUMOperationJourneyStepType("start")
RUMOperationJourneyStepType.UPDATE = RUMOperationJourneyStepType("update")
RUMOperationJourneyStepType.STOP = RUMOperationJourneyStepType("stop")
RUMOperationJourneyStepType.ERROR = RUMOperationJourneyStepType("error")
RUMOperationJourneyStepType.ABANDONED = RUMOperationJourneyStepType("abandoned")
