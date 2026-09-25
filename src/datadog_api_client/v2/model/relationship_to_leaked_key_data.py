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
    from datadog_api_client.v2.model.leaked_key_type import LeakedKeyType


class RelationshipToLeakedKeyData(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.leaked_key_type import LeakedKeyType

        return {
            "id": (str,),
            "type": (LeakedKeyType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: LeakedKeyType, **kwargs):
        """
        Relationship to the leak the access token was found in.

        :param id: A unique identifier that represents the leak.
        :type id: str

        :param type: The definition of LeakedKeyType object.
        :type type: LeakedKeyType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
