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
    from datadog_api_client.v2.model.change_event_custom_attributes_author_type import (
        ChangeEventCustomAttributesAuthorType,
    )


class ChangeEventCustomAttributesAuthor(ModelNormal):
    validations = {
        "name": {
            "max_length": 128,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_event_custom_attributes_author_type import (
            ChangeEventCustomAttributesAuthorType,
        )

        return {
            "name": (str,),
            "type": (ChangeEventCustomAttributesAuthorType,),
        }

    attribute_map = {
        "name": "name",
        "type": "type",
    }

    def __init__(self_, name: str, type: ChangeEventCustomAttributesAuthorType, **kwargs):
        """
        Object representing the entity which made the change. Optional field but if provided should include ``type`` and ``name``.

        :param name: Author's name. Limited to 128 characters.
        :type name: str

        :param type: Author's type.
        :type type: ChangeEventCustomAttributesAuthorType
        """
        super().__init__(kwargs)

        self_.name = name
        self_.type = type
