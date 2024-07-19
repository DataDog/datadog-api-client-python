# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
    from datadog_api_client.v2.model.nullable_relationship_to_user import NullableRelationshipToUser


class APIKeyRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_user import RelationshipToUser
        from datadog_api_client.v2.model.nullable_relationship_to_user import NullableRelationshipToUser

        return {
            "created_by": (RelationshipToUser,),
            "modified_by": (NullableRelationshipToUser,),
        }

    attribute_map = {
        "created_by": "created_by",
        "modified_by": "modified_by",
    }

    def __init__(
        self_,
        created_by: Union[RelationshipToUser, UnsetType] = unset,
        modified_by: Union[NullableRelationshipToUser, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Resources related to the API key.

        :param created_by: Relationship to user.
        :type created_by: RelationshipToUser, optional

        :param modified_by: Relationship to user.
        :type modified_by: NullableRelationshipToUser, none_type, optional
        """
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if modified_by is not unset:
            kwargs["modified_by"] = modified_by
        super().__init__(kwargs)
