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
    from datadog_api_client.v2.model.access_token_owner_type import AccessTokenOwnerType


class RelationshipToAccessTokenOwnerData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.access_token_owner_type import AccessTokenOwnerType

        return {
            "id": (str,),
            "type": (AccessTokenOwnerType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: AccessTokenOwnerType, **kwargs):
        """
        Relationship to the access token's owner.

        :param id: A unique identifier that represents the owner.
        :type id: str

        :param type: Owner resource type. Either a user or a service account.
        :type type: AccessTokenOwnerType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
