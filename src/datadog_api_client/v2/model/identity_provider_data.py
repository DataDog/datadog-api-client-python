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
    from datadog_api_client.v2.model.identity_provider_attributes import IdentityProviderAttributes
    from datadog_api_client.v2.model.identity_provider_type import IdentityProviderType


class IdentityProviderData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.identity_provider_attributes import IdentityProviderAttributes
        from datadog_api_client.v2.model.identity_provider_type import IdentityProviderType

        return {
            "attributes": (IdentityProviderAttributes,),
            "id": (str,),
            "type": (IdentityProviderType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: IdentityProviderAttributes, id: str, type: IdentityProviderType, **kwargs):
        """
        Data object representing an organization identity provider.

        :param attributes: Attributes of an organization identity provider.
        :type attributes: IdentityProviderAttributes

        :param id: The unique identifier of the identity provider.
        :type id: str

        :param type: The resource type for identity providers.
        :type type: IdentityProviderType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
