# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.relationship_to_leaked_key import RelationshipToLeakedKey
    from datadog_api_client.v2.model.relationship_to_access_token_owner import RelationshipToAccessTokenOwner


class AccessTokenListItemRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_leaked_key import RelationshipToLeakedKey
        from datadog_api_client.v2.model.relationship_to_access_token_owner import RelationshipToAccessTokenOwner

        return {
            "leak_information": (RelationshipToLeakedKey,),
            "owned_by": (RelationshipToAccessTokenOwner,),
        }

    attribute_map = {
        "leak_information": "leak_information",
        "owned_by": "owned_by",
    }

    def __init__(
        self_,
        leak_information: Union[RelationshipToLeakedKey, UnsetType] = unset,
        owned_by: Union[RelationshipToAccessTokenOwner, UnsetType] = unset,
        **kwargs,
    ):
        """
        Resources related to the access token entry in the mixed list response.

        :param leak_information: Relationship to the leak the access token was found in. ``data`` is null when the access token has not been detected as leaked.
        :type leak_information: RelationshipToLeakedKey, optional

        :param owned_by: Relationship to the access token's owner.
        :type owned_by: RelationshipToAccessTokenOwner, optional
        """
        if leak_information is not unset:
            kwargs["leak_information"] = leak_information
        if owned_by is not unset:
            kwargs["owned_by"] = owned_by
        super().__init__(kwargs)
