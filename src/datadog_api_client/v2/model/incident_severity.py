# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentSeverity(ModelSimple):
    """
    The incident severity.

    :param value: Must be one of ["UNKNOWN", "SEV-1", "SEV-2", "SEV-3", "SEV-4", "SEV-5"].
    :type value: str
    """

    allowed_values = {
        "UNKNOWN",
        "SEV-1",
        "SEV-2",
        "SEV-3",
        "SEV-4",
        "SEV-5",
    }
    UNKNOWN: ClassVar["IncidentSeverity"]
    SEV_1: ClassVar["IncidentSeverity"]
    SEV_2: ClassVar["IncidentSeverity"]
    SEV_3: ClassVar["IncidentSeverity"]
    SEV_4: ClassVar["IncidentSeverity"]
    SEV_5: ClassVar["IncidentSeverity"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentSeverity.UNKNOWN = IncidentSeverity("UNKNOWN")
IncidentSeverity.SEV_1 = IncidentSeverity("SEV-1")
IncidentSeverity.SEV_2 = IncidentSeverity("SEV-2")
IncidentSeverity.SEV_3 = IncidentSeverity("SEV-3")
IncidentSeverity.SEV_4 = IncidentSeverity("SEV-4")
IncidentSeverity.SEV_5 = IncidentSeverity("SEV-5")
