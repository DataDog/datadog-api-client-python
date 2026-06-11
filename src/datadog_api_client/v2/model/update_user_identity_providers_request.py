# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.user_relationship_identity_provider_data import (
        UserRelationshipIdentityProviderData,
    )


class UpdateUserIdentityProvidersRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_relationship_identity_provider_data import (
            UserRelationshipIdentityProviderData,
        )

        return {
            "data": ([UserRelationshipIdentityProviderData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[UserRelationshipIdentityProviderData], **kwargs):
        """
        Request body for setting identity provider overrides for a user.

        :param data: List of identity provider resource identifiers for a relationship update.
        :type data: [UserRelationshipIdentityProviderData]
        """
        super().__init__(kwargs)

        self_.data = data
