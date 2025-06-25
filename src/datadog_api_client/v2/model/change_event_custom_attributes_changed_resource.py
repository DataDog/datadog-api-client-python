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
    from datadog_api_client.v2.model.change_event_custom_attributes_changed_resource_type import (
        ChangeEventCustomAttributesChangedResourceType,
    )


class ChangeEventCustomAttributesChangedResource(ModelNormal):
    validations = {
        "name": {
            "max_length": 128,
            "min_length": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_event_custom_attributes_changed_resource_type import (
            ChangeEventCustomAttributesChangedResourceType,
        )

        return {
            "name": (str,),
            "type": (ChangeEventCustomAttributesChangedResourceType,),
        }

    attribute_map = {
        "name": "name",
        "type": "type",
    }

    def __init__(self_, name: str, type: ChangeEventCustomAttributesChangedResourceType, **kwargs):
        """
        A uniquely identified resource.

        :param name: The name of the resource that was changed. Limited to 128 characters.
        :type name: str

        :param type: The type of the resource that was changed.
        :type type: ChangeEventCustomAttributesChangedResourceType
        """
        super().__init__(kwargs)

        self_.name = name
        self_.type = type
