# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentUserDefinedFieldCollected(ModelSimple):
    """
    The lifecycle stage at which the app prompts users to fill out this field. Cannot be set on required fields.

    :param value: Must be one of ["active", "stable", "resolved", "completed"].
    :type value: str
    """

    allowed_values = {
        "active",
        "stable",
        "resolved",
        "completed",
    }
    ACTIVE: ClassVar["IncidentUserDefinedFieldCollected"]
    STABLE: ClassVar["IncidentUserDefinedFieldCollected"]
    RESOLVED: ClassVar["IncidentUserDefinedFieldCollected"]
    COMPLETED: ClassVar["IncidentUserDefinedFieldCollected"]

    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentUserDefinedFieldCollected.ACTIVE = IncidentUserDefinedFieldCollected("active")
IncidentUserDefinedFieldCollected.STABLE = IncidentUserDefinedFieldCollected("stable")
IncidentUserDefinedFieldCollected.RESOLVED = IncidentUserDefinedFieldCollected("resolved")
IncidentUserDefinedFieldCollected.COMPLETED = IncidentUserDefinedFieldCollected("completed")
