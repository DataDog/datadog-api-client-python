# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.postmortem_attachment_request_attributes import (
        PostmortemAttachmentRequestAttributes,
    )
    from datadog_api_client.v2.model.incident_attachment_type import IncidentAttachmentType


class PostmortemAttachmentRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.postmortem_attachment_request_attributes import (
            PostmortemAttachmentRequestAttributes,
        )
        from datadog_api_client.v2.model.incident_attachment_type import IncidentAttachmentType

        return {
            "attributes": (PostmortemAttachmentRequestAttributes,),
            "type": (IncidentAttachmentType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: PostmortemAttachmentRequestAttributes, type: IncidentAttachmentType, **kwargs):
        """
        Postmortem attachment data

        :param attributes: Postmortem attachment attributes
        :type attributes: PostmortemAttachmentRequestAttributes

        :param type: The incident attachment resource type.
        :type type: IncidentAttachmentType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
