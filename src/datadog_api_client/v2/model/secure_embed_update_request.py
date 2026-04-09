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
    from datadog_api_client.v2.model.secure_embed_update_request_data import SecureEmbedUpdateRequestData


class SecureEmbedUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.secure_embed_update_request_data import SecureEmbedUpdateRequestData

        return {
            "data": (SecureEmbedUpdateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SecureEmbedUpdateRequestData, **kwargs):
        """
        Request to update a secure embed shared dashboard.

        :param data: Data object for updating a secure embed.
        :type data: SecureEmbedUpdateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
