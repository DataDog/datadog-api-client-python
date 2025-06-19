# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
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
    validations = {
        "impacted_resources": {
            "max_items": 100,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

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
            "change_metadata": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "changed_resource": (ChangeEventCustomAttributesChangedResource,),
            "impacted_resources": ([ChangeEventCustomAttributesImpactedResourcesItems],),
            "new_value": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "prev_value": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
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
        change_metadata: Union[Dict[str, Any], UnsetType] = unset,
        impacted_resources: Union[List[ChangeEventCustomAttributesImpactedResourcesItems], UnsetType] = unset,
        new_value: Union[Dict[str, Any], UnsetType] = unset,
        prev_value: Union[Dict[str, Any], UnsetType] = unset,
        **kwargs,
    ):
        """
        Change event attributes.

        :param author: The entity that made the change. Optional, if provided it must include ``type`` and ``name``.
        :type author: ChangeEventCustomAttributesAuthor, optional

        :param change_metadata: Free form JSON object with information related to the ``change`` event. Supports up to 100 properties per object and a maximum nesting depth of 10 levels.
        :type change_metadata: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param changed_resource: A uniquely identified resource.
        :type changed_resource: ChangeEventCustomAttributesChangedResource

        :param impacted_resources: A list of resources impacted by this change. It is recommended to provide an impacted resource to display
            the change event at the correct location. Only resources of type ``service`` are supported. Maximum of 100 impacted resources allowed.
        :type impacted_resources: [ChangeEventCustomAttributesImpactedResourcesItems], optional

        :param new_value: Free form JSON object representing the new state of the changed resource.
        :type new_value: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param prev_value: Free form JSON object representing the previous state of the changed resource.
        :type prev_value: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional
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
