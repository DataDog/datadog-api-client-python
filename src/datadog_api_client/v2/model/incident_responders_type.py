# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentRespondersType(ModelSimple):
    """
    The incident responders type.

    :param value: If omitted defaults to "incident_responders". Must be one of ["incident_responders"].
    :type value: str
    """

    allowed_values = {
        "incident_responders",
    }
    INCIDENT_RESPONDERS: ClassVar["IncidentRespondersType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentRespondersType.INCIDENT_RESPONDERS = IncidentRespondersType("incident_responders")
