# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentImpactType(ModelSimple):
    """
    Incident impact resource type.

    :param value: If omitted defaults to "incident_impacts". Must be one of ["incident_impacts"].
    :type value: str
    """

    allowed_values = {
        "incident_impacts",
    }
    INCIDENT_IMPACTS: ClassVar["IncidentImpactType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentImpactType.INCIDENT_IMPACTS = IncidentImpactType("incident_impacts")
