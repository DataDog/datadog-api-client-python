# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.change_event_custom_attributes_author import ChangeEventCustomAttributesAuthor
    from datadog_api_client.v2.model.change_event_custom_attributes_changed_resource import (
        ChangeEventCustomAttributesChangedResource,
    )
    from datadog_api_client.v2.model.change_event_custom_attributes_impacted_resources_items import (
        ChangeEventCustomAttributesImpactedResourcesItems,
    )


class ChangeEventCustomAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_event_custom_attributes_author import ChangeEventCustomAttributesAuthor
        from datadog_api_client.v2.model.change_event_custom_attributes_changed_resource import (
            ChangeEventCustomAttributesChangedResource,
        )
        from datadog_api_client.v2.model.change_event_custom_attributes_impacted_resources_items import (
            ChangeEventCustomAttributesImpactedResourcesItems,
        )

        return {
            "author": (ChangeEventCustomAttributesAuthor,),
            "change_metadata": (dict,),
            "changed_resource": (ChangeEventCustomAttributesChangedResource,),
            "impacted_resources": ([ChangeEventCustomAttributesImpactedResourcesItems],),
            "new_value": (dict,),
            "prev_value": (dict,),
        }

    attribute_map = {
        "author": "author",
        "change_metadata": "change_metadata",
        "changed_resource": "changed_resource",
        "impacted_resources": "impacted_resources",
        "new_value": "new_value",
        "prev_value": "prev_value",
    }

    def __init__(
        self_,
        changed_resource: ChangeEventCustomAttributesChangedResource,
        author: Union[ChangeEventCustomAttributesAuthor, UnsetType] = unset,
        change_metadata: Union[dict, UnsetType] = unset,
        impacted_resources: Union[List[ChangeEventCustomAttributesImpactedResourcesItems], UnsetType] = unset,
        new_value: Union[dict, UnsetType] = unset,
        prev_value: Union[dict, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object representing custom event attributes.

        :param author: Object representing the entity which made the change. Optional field but if provided should include ``type`` and ``name``.
        :type author: ChangeEventCustomAttributesAuthor, optional

        :param change_metadata: Free form object with any related information of the ``change`` event.
        :type change_metadata: dict, optional

        :param changed_resource: Object representing a uniquely identified resource. Only the resource type ``feature_flag`` is supported.
        :type changed_resource: ChangeEventCustomAttributesChangedResource

        :param impacted_resources: A list of resources impacted by this change. At least one resource is required. Only resources
            of type ``service`` are supported.
        :type impacted_resources: [ChangeEventCustomAttributesImpactedResourcesItems], optional

        :param new_value: Free form object to track new value of the changed resource.
        :type new_value: dict, optional

        :param prev_value: Free form object to track previous value of the changed resource.
        :type prev_value: dict, optional
        """
        if author is not unset:
            kwargs["author"] = author
        if change_metadata is not unset:
            kwargs["change_metadata"] = change_metadata
        if impacted_resources is not unset:
            kwargs["impacted_resources"] = impacted_resources
        if new_value is not unset:
            kwargs["new_value"] = new_value
        if prev_value is not unset:
            kwargs["prev_value"] = prev_value
        super().__init__(kwargs)

        self_.changed_resource = changed_resource
