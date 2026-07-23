# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ScheduleTriggerOverlapBehavior(ModelSimple):
    """
    Controls whether a scheduled workflow run may start while another instance is still running.

    :param value: If omitted defaults to "EXCLUSIVE_RUN". Must be one of ["EXCLUSIVE_RUN", "OVERLAP_ALLOWED"].
    :type value: str
    """

    allowed_values = {
        "EXCLUSIVE_RUN",
        "OVERLAP_ALLOWED",
    }
    EXCLUSIVE_RUN: ClassVar["ScheduleTriggerOverlapBehavior"]
    OVERLAP_ALLOWED: ClassVar["ScheduleTriggerOverlapBehavior"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ScheduleTriggerOverlapBehavior.EXCLUSIVE_RUN = ScheduleTriggerOverlapBehavior("EXCLUSIVE_RUN")
ScheduleTriggerOverlapBehavior.OVERLAP_ALLOWED = ScheduleTriggerOverlapBehavior("OVERLAP_ALLOWED")
