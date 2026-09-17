# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GeneralInvestigationTriggerType(ModelSimple):
    """
    The type of general investigation trigger.

    :param value: If omitted defaults to "general_investigation". Must be one of ["general_investigation"].
    :type value: str
    """

    allowed_values = {
        "general_investigation",
    }
    GENERAL_INVESTIGATION: ClassVar["GeneralInvestigationTriggerType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GeneralInvestigationTriggerType.GENERAL_INVESTIGATION = GeneralInvestigationTriggerType("general_investigation")
