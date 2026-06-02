# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentRuleResponseType(ModelSimple):
    """
    Incident rule response resource type.

    :param value: If omitted defaults to "incidents_rules". Must be one of ["incidents_rules"].
    :type value: str
    """

    allowed_values = {
        "incidents_rules",
    }
    INCIDENTS_RULES: ClassVar["IncidentRuleResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentRuleResponseType.INCIDENTS_RULES = IncidentRuleResponseType("incidents_rules")
