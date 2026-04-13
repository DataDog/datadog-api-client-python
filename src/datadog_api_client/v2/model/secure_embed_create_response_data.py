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
    from datadog_api_client.v2.model.secure_embed_create_response_attributes import SecureEmbedCreateResponseAttributes
    from datadog_api_client.v2.model.secure_embed_create_response_type import SecureEmbedCreateResponseType


class SecureEmbedCreateResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.secure_embed_create_response_attributes import (
            SecureEmbedCreateResponseAttributes,
        )
        from datadog_api_client.v2.model.secure_embed_create_response_type import SecureEmbedCreateResponseType

        return {
            "attributes": (SecureEmbedCreateResponseAttributes,),
            "id": (str,),
            "type": (SecureEmbedCreateResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: SecureEmbedCreateResponseAttributes, id: str, type: SecureEmbedCreateResponseType, **kwargs
    ):
        """
        Data object for a secure embed create response.

        :param attributes: Attributes of a newly created secure embed shared dashboard.
        :type attributes: SecureEmbedCreateResponseAttributes

        :param id: Internal share ID.
        :type id: str

        :param type: Resource type for secure embed create responses.
        :type type: SecureEmbedCreateResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
