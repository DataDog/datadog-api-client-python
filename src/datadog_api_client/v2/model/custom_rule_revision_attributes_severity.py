# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CustomRuleRevisionAttributesSeverity(ModelSimple):
    """
    Rule severity

    :param value: Must be one of ["ERROR", "WARNING", "NOTICE"].
    :type value: str
    """

    allowed_values = {
        "ERROR",
        "WARNING",
        "NOTICE",
    }
    ERROR: ClassVar["CustomRuleRevisionAttributesSeverity"]
    WARNING: ClassVar["CustomRuleRevisionAttributesSeverity"]
    NOTICE: ClassVar["CustomRuleRevisionAttributesSeverity"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CustomRuleRevisionAttributesSeverity.ERROR = CustomRuleRevisionAttributesSeverity("ERROR")
CustomRuleRevisionAttributesSeverity.WARNING = CustomRuleRevisionAttributesSeverity("WARNING")
CustomRuleRevisionAttributesSeverity.NOTICE = CustomRuleRevisionAttributesSeverity("NOTICE")
