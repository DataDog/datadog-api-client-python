# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_attachment_link_attributes_attachment_object import (
        IncidentAttachmentLinkAttributesAttachmentObject,
    )
    from datadog_api_client.v2.model.incident_attachment_link_attachment_type import (
        IncidentAttachmentLinkAttachmentType,
    )


class IncidentAttachmentLinkAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_attachment_link_attributes_attachment_object import (
            IncidentAttachmentLinkAttributesAttachmentObject,
        )
        from datadog_api_client.v2.model.incident_attachment_link_attachment_type import (
            IncidentAttachmentLinkAttachmentType,
        )

        return {
            "attachment": (IncidentAttachmentLinkAttributesAttachmentObject,),
            "attachment_type": (IncidentAttachmentLinkAttachmentType,),
            "modified": (datetime,),
        }

    attribute_map = {
        "attachment": "attachment",
        "attachment_type": "attachment_type",
        "modified": "modified",
    }
    read_only_vars = {
        "modified",
    }

    def __init__(
        self_,
        attachment: IncidentAttachmentLinkAttributesAttachmentObject,
        attachment_type: IncidentAttachmentLinkAttachmentType,
        modified: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes object for a link attachment.

        :param attachment: The link attachment.
        :type attachment: IncidentAttachmentLinkAttributesAttachmentObject

        :param attachment_type: The type of link attachment attributes.
        :type attachment_type: IncidentAttachmentLinkAttachmentType

        :param modified: Timestamp when the incident attachment link was last modified.
        :type modified: datetime, optional
        """
        if modified is not unset:
            kwargs["modified"] = modified
        super().__init__(kwargs)

        self_.attachment = attachment
        self_.attachment_type = attachment_type
