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
    from datadog_api_client.v2.model.secure_embed_get_response_attributes import SecureEmbedGetResponseAttributes
    from datadog_api_client.v2.model.secure_embed_get_response_type import SecureEmbedGetResponseType


class SecureEmbedGetResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.secure_embed_get_response_attributes import SecureEmbedGetResponseAttributes
        from datadog_api_client.v2.model.secure_embed_get_response_type import SecureEmbedGetResponseType

        return {
            "attributes": (SecureEmbedGetResponseAttributes,),
            "id": (str,),
            "type": (SecureEmbedGetResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: SecureEmbedGetResponseAttributes, id: str, type: SecureEmbedGetResponseType, **kwargs
    ):
        """
        Data object for a secure embed get response.

        :param attributes: Attributes of an existing secure embed shared dashboard.
        :type attributes: SecureEmbedGetResponseAttributes

        :param id: Internal share ID.
        :type id: str

        :param type: Resource type for secure embed get responses.
        :type type: SecureEmbedGetResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
