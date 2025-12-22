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
    from datadog_api_client.v2.model.patch_attachment_request_data_attributes_attachment import (
        PatchAttachmentRequestDataAttributesAttachment,
    )


class PatchAttachmentRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_attachment_request_data_attributes_attachment import (
            PatchAttachmentRequestDataAttributesAttachment,
        )

        return {
            "attachment": (PatchAttachmentRequestDataAttributesAttachment,),
        }

    attribute_map = {
        "attachment": "attachment",
    }

    def __init__(self_, attachment: Union[PatchAttachmentRequestDataAttributesAttachment, UnsetType] = unset, **kwargs):
        """


        :param attachment:
        :type attachment: PatchAttachmentRequestDataAttributesAttachment, optional
        """
        if attachment is not unset:
            kwargs["attachment"] = attachment
        super().__init__(kwargs)
