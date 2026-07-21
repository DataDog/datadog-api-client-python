# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentGoogleMeetConfigurationType(ModelSimple):
    """
    Google Meet configuration resource type.

    :param value: If omitted defaults to "google_meet_configurations". Must be one of ["google_meet_configurations"].
    :type value: str
    """

    allowed_values = {
        "google_meet_configurations",
    }
    GOOGLE_MEET_CONFIGURATIONS: ClassVar["IncidentGoogleMeetConfigurationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentGoogleMeetConfigurationType.GOOGLE_MEET_CONFIGURATIONS = IncidentGoogleMeetConfigurationType(
    "google_meet_configurations"
)
