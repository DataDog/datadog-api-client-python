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
    from datadog_api_client.v2.model.secure_embed_update_request_attributes import SecureEmbedUpdateRequestAttributes
    from datadog_api_client.v2.model.secure_embed_update_request_type import SecureEmbedUpdateRequestType


class SecureEmbedUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.secure_embed_update_request_attributes import (
            SecureEmbedUpdateRequestAttributes,
        )
        from datadog_api_client.v2.model.secure_embed_update_request_type import SecureEmbedUpdateRequestType

        return {
            "attributes": (SecureEmbedUpdateRequestAttributes,),
            "type": (SecureEmbedUpdateRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: SecureEmbedUpdateRequestAttributes, type: SecureEmbedUpdateRequestType, **kwargs):
        """
        Data object for updating a secure embed.

        :param attributes: Attributes for updating a secure embed shared dashboard. All fields are optional.
        :type attributes: SecureEmbedUpdateRequestAttributes

        :param type: Resource type for secure embed update requests.
        :type type: SecureEmbedUpdateRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
