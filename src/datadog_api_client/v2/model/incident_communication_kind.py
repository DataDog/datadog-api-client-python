# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentCommunicationKind(ModelSimple):
    """
    The kind of communication.

    :param value: Must be one of ["manual", "automated"].
    :type value: str
    """

    allowed_values = {
        "manual",
        "automated",
    }
    MANUAL: ClassVar["IncidentCommunicationKind"]
    AUTOMATED: ClassVar["IncidentCommunicationKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentCommunicationKind.MANUAL = IncidentCommunicationKind("manual")
IncidentCommunicationKind.AUTOMATED = IncidentCommunicationKind("automated")
