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
    from datadog_api_client.v2.model.attachment_data_attributes_attachment import AttachmentDataAttributesAttachment
    from datadog_api_client.v2.model.attachment_data_attributes_attachment_type import (
        AttachmentDataAttributesAttachmentType,
    )


class AttachmentDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.attachment_data_attributes_attachment import AttachmentDataAttributesAttachment
        from datadog_api_client.v2.model.attachment_data_attributes_attachment_type import (
            AttachmentDataAttributesAttachmentType,
        )

        return {
            "attachment": (AttachmentDataAttributesAttachment,),
            "attachment_type": (AttachmentDataAttributesAttachmentType,),
            "modified": (datetime,),
        }

    attribute_map = {
        "attachment": "attachment",
        "attachment_type": "attachment_type",
        "modified": "modified",
    }

    def __init__(
        self_,
        attachment: Union[AttachmentDataAttributesAttachment, UnsetType] = unset,
        attachment_type: Union[AttachmentDataAttributesAttachmentType, UnsetType] = unset,
        modified: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attachment:
        :type attachment: AttachmentDataAttributesAttachment, optional

        :param attachment_type:
        :type attachment_type: AttachmentDataAttributesAttachmentType, optional

        :param modified:
        :type modified: datetime, optional
        """
        if attachment is not unset:
            kwargs["attachment"] = attachment
        if attachment_type is not unset:
            kwargs["attachment_type"] = attachment_type
        if modified is not unset:
            kwargs["modified"] = modified
        super().__init__(kwargs)
