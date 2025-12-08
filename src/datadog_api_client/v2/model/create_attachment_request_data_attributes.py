# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_attachment_request_data_attributes_attachment import (
        CreateAttachmentRequestDataAttributesAttachment,
    )
    from datadog_api_client.v2.model.attachment_data_attributes_attachment_type import (
        AttachmentDataAttributesAttachmentType,
    )


class CreateAttachmentRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_attachment_request_data_attributes_attachment import (
            CreateAttachmentRequestDataAttributesAttachment,
        )
        from datadog_api_client.v2.model.attachment_data_attributes_attachment_type import (
            AttachmentDataAttributesAttachmentType,
        )

        return {
            "attachment": (CreateAttachmentRequestDataAttributesAttachment,),
            "attachment_type": (AttachmentDataAttributesAttachmentType,),
        }

    attribute_map = {
        "attachment": "attachment",
        "attachment_type": "attachment_type",
    }

    def __init__(
        self_,
        attachment: Union[CreateAttachmentRequestDataAttributesAttachment, UnsetType] = unset,
        attachment_type: Union[AttachmentDataAttributesAttachmentType, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attachment:
        :type attachment: CreateAttachmentRequestDataAttributesAttachment, optional

        :param attachment_type:
        :type attachment_type: AttachmentDataAttributesAttachmentType, optional
        """
        if attachment is not unset:
            kwargs["attachment"] = attachment
        if attachment_type is not unset:
            kwargs["attachment_type"] = attachment_type
        super().__init__(kwargs)
