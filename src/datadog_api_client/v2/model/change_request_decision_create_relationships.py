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
    from datadog_api_client.v2.model.change_request_user_relationship import ChangeRequestUserRelationship


class ChangeRequestDecisionCreateRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_request_user_relationship import ChangeRequestUserRelationship

        return {
            "requested_user": (ChangeRequestUserRelationship,),
        }

    attribute_map = {
        "requested_user": "requested_user",
    }

    def __init__(self_, requested_user: Union[ChangeRequestUserRelationship, UnsetType] = unset, **kwargs):
        """
        Relationships for creating a change request decision.

        :param requested_user: Relationship to a user.
        :type requested_user: ChangeRequestUserRelationship, optional
        """
        if requested_user is not unset:
            kwargs["requested_user"] = requested_user
        super().__init__(kwargs)
