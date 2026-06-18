# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.delegated_token_attributes import DelegatedTokenAttributes
    from datadog_api_client.v2.model.delegated_token_type import DelegatedTokenType


class DelegatedTokenData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.delegated_token_attributes import DelegatedTokenAttributes
        from datadog_api_client.v2.model.delegated_token_type import DelegatedTokenType

        return {
            "attributes": (DelegatedTokenAttributes,),
            "id": (UUID,),
            "type": (DelegatedTokenType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: DelegatedTokenAttributes, id: UUID, type: DelegatedTokenType, **kwargs):
        """
        A delegated token resource.

        :param attributes: Attributes of a delegated token.
        :type attributes: DelegatedTokenAttributes

        :param id: A random UUID assigned to this token issuance.
        :type id: UUID

        :param type: The resource type for a delegated token.
        :type type: DelegatedTokenType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
