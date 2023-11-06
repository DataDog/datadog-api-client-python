# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class IncidentIntegrationMetadataType(StringEnum):
    """
    Integration metadata resource type.

    :param value: If omitted defaults to "incident_integrations". Must be one of ["incident_integrations"].
    :type value: str
    """

    allowed_values = {
        "incident_integrations",
    }
    INCIDENT_INTEGRATIONS: ClassVar["IncidentIntegrationMetadataType"]


IncidentIntegrationMetadataType.INCIDENT_INTEGRATIONS = IncidentIntegrationMetadataType("incident_integrations")
