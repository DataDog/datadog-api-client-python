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
    from datadog_api_client.v2.model.secure_embed_update_response_attributes import SecureEmbedUpdateResponseAttributes
    from datadog_api_client.v2.model.secure_embed_update_response_type import SecureEmbedUpdateResponseType


class SecureEmbedUpdateResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.secure_embed_update_response_attributes import (
            SecureEmbedUpdateResponseAttributes,
        )
        from datadog_api_client.v2.model.secure_embed_update_response_type import SecureEmbedUpdateResponseType

        return {
            "attributes": (SecureEmbedUpdateResponseAttributes,),
            "id": (str,),
            "type": (SecureEmbedUpdateResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: SecureEmbedUpdateResponseAttributes, id: str, type: SecureEmbedUpdateResponseType, **kwargs
    ):
        """
        Data object for a secure embed update response.

        :param attributes: Attributes of an updated secure embed shared dashboard.
        :type attributes: SecureEmbedUpdateResponseAttributes

        :param id: Internal share ID.
        :type id: str

        :param type: Resource type for secure embed update responses.
        :type type: SecureEmbedUpdateResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
