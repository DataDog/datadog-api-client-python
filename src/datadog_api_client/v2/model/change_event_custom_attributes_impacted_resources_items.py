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
    from datadog_api_client.v2.model.change_event_custom_attributes_impacted_resources_items_type import (
        ChangeEventCustomAttributesImpactedResourcesItemsType,
    )


class ChangeEventCustomAttributesImpactedResourcesItems(ModelNormal):
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
        from datadog_api_client.v2.model.change_event_custom_attributes_impacted_resources_items_type import (
            ChangeEventCustomAttributesImpactedResourcesItemsType,
        )

        return {
            "name": (str,),
            "type": (ChangeEventCustomAttributesImpactedResourcesItemsType,),
        }

    attribute_map = {
        "name": "name",
        "type": "type",
    }

    def __init__(self_, name: str, type: ChangeEventCustomAttributesImpactedResourcesItemsType, **kwargs):
        """
        Object representing a uniquely identified resource.

        :param name: The name of the impacted resource. Limited to 128 characters.
        :type name: str

        :param type: The type of the impacted resource.
        :type type: ChangeEventCustomAttributesImpactedResourcesItemsType
        """
        super().__init__(kwargs)

        self_.name = name
        self_.type = type
