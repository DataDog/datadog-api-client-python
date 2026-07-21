# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentRuleType(ModelSimple):
    """
    Incident rule resource type.

    :param value: If omitted defaults to "incident_rules". Must be one of ["incident_rules"].
    :type value: str
    """

    allowed_values = {
        "incident_rules",
    }
    INCIDENT_RULES: ClassVar["IncidentRuleType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentRuleType.INCIDENT_RULES = IncidentRuleType("incident_rules")
