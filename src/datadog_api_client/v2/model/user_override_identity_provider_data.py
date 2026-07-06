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
    from datadog_api_client.v2.model.user_override_identity_provider_attributes import (
        UserOverrideIdentityProviderAttributes,
    )
    from datadog_api_client.v2.model.user_override_identity_provider_data_type import (
        UserOverrideIdentityProviderDataType,
    )


class UserOverrideIdentityProviderData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_override_identity_provider_attributes import (
            UserOverrideIdentityProviderAttributes,
        )
        from datadog_api_client.v2.model.user_override_identity_provider_data_type import (
            UserOverrideIdentityProviderDataType,
        )

        return {
            "attributes": (UserOverrideIdentityProviderAttributes,),
            "id": (str,),
            "type": (UserOverrideIdentityProviderDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: UserOverrideIdentityProviderAttributes,
        id: str,
        type: UserOverrideIdentityProviderDataType,
        **kwargs,
    ):
        """
        Data object representing a user identity provider override.

        :param attributes: Attributes of an identity provider override for a user.
        :type attributes: UserOverrideIdentityProviderAttributes

        :param id: The unique identifier of the identity provider.
        :type id: str

        :param type: The resource type for identity providers.
        :type type: UserOverrideIdentityProviderDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
