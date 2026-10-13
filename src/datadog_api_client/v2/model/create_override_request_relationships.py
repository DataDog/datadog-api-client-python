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
    from datadog_api_client.v2.model.override_relationships_user import OverrideRelationshipsUser


class CreateOverrideRequestRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.override_relationships_user import OverrideRelationshipsUser

        return {
            "overridden_user": (OverrideRelationshipsUser,),
            "user": (OverrideRelationshipsUser,),
        }

    attribute_map = {
        "overridden_user": "overridden_user",
        "user": "user",
    }

    def __init__(
        self_,
        overridden_user: Union[OverrideRelationshipsUser, UnsetType] = unset,
        user: Union[OverrideRelationshipsUser, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationships to set when creating an on-call schedule override.

        :param overridden_user: Defines the relationship between an override and one of its associated users.
        :type overridden_user: OverrideRelationshipsUser, optional

        :param user: Defines the relationship between an override and one of its associated users.
        :type user: OverrideRelationshipsUser, optional
        """
        if overridden_user is not unset:
            kwargs["overridden_user"] = overridden_user
        if user is not unset:
            kwargs["user"] = user
        super().__init__(kwargs)
