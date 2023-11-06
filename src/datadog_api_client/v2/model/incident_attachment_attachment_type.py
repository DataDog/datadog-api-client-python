# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class IncidentAttachmentAttachmentType(StringEnum):
    """
    The type of the incident attachment attributes.

    :param value: Must be one of ["link", "postmortem"].
    :type value: str
    """

    allowed_values = {
        "link",
        "postmortem",
    }
    LINK: ClassVar["IncidentAttachmentAttachmentType"]
    POSTMORTEM: ClassVar["IncidentAttachmentAttachmentType"]


IncidentAttachmentAttachmentType.LINK = IncidentAttachmentAttachmentType("link")
IncidentAttachmentAttachmentType.POSTMORTEM = IncidentAttachmentAttachmentType("postmortem")
