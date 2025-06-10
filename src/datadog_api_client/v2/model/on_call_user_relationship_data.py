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
    from datadog_api_client.v2.model.on_call_user_relationship_type import OnCallUserRelationshipType


class OnCallUserRelationshipData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_call_user_relationship_type import OnCallUserRelationshipType

        return {
            "id": (str,),
            "type": (OnCallUserRelationshipType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, id: Union[str, UnsetType] = unset, type: Union[OnCallUserRelationshipType, UnsetType] = unset, **kwargs
    ):
        """
        The definition of ``OnCallUserRelationshipData`` object.

        :param id: The ID of the user.
        :type id: str, optional

        :param type: The definition of ``OnCallUserRelationshipType`` object.
        :type type: OnCallUserRelationshipType, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
