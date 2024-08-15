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
    from datadog_api_client.v2.model.leaked_key_attributes import LeakedKeyAttributes
    from datadog_api_client.v2.model.leaked_key_type import LeakedKeyType


class LeakedKey(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.leaked_key_attributes import LeakedKeyAttributes
        from datadog_api_client.v2.model.leaked_key_type import LeakedKeyType

        return {
            "attributes": (LeakedKeyAttributes,),
            "id": (str,),
            "type": (LeakedKeyType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: LeakedKeyAttributes, id: str, type: LeakedKeyType, **kwargs):
        """
        The definition of LeakedKey object.

        :param attributes: The definition of LeakedKeyAttributes object.
        :type attributes: LeakedKeyAttributes

        :param id: The LeakedKey id.
        :type id: str

        :param type: The definition of LeakedKeyType object.
        :type type: LeakedKeyType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
