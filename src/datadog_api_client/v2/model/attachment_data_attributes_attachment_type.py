# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AttachmentDataAttributesAttachmentType(ModelSimple):
    """


    :param value: Must be one of ["postmortem", "link"].
    :type value: str
    """

    allowed_values = {
        "postmortem",
        "link",
    }
    POSTMORTEM: ClassVar["AttachmentDataAttributesAttachmentType"]
    LINK: ClassVar["AttachmentDataAttributesAttachmentType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AttachmentDataAttributesAttachmentType.POSTMORTEM = AttachmentDataAttributesAttachmentType("postmortem")
AttachmentDataAttributesAttachmentType.LINK = AttachmentDataAttributesAttachmentType("link")
