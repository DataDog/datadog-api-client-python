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
    from datadog_api_client.v2.model.change_event_attributes_author import ChangeEventAttributesAuthor
    from datadog_api_client.v2.model.change_event_attributes_changed_resource import (
        ChangeEventAttributesChangedResource,
    )
    from datadog_api_client.v2.model.event_system_attributes import EventSystemAttributes
    from datadog_api_client.v2.model.change_event_attributes_impacted_resources_item import (
        ChangeEventAttributesImpactedResourcesItem,
    )


class ChangeEventAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_event_attributes_author import ChangeEventAttributesAuthor
        from datadog_api_client.v2.model.change_event_attributes_changed_resource import (
            ChangeEventAttributesChangedResource,
        )
        from datadog_api_client.v2.model.event_system_attributes import EventSystemAttributes
        from datadog_api_client.v2.model.change_event_attributes_impacted_resources_item import (
            ChangeEventAttributesImpactedResourcesItem,
        )

        return {
            "aggregation_key": (str,),
            "author": (ChangeEventAttributesAuthor,),
            "change_metadata": (dict,),
            "changed_resource": (ChangeEventAttributesChangedResource,),
            "evt": (EventSystemAttributes,),
            "impacted_resources": ([ChangeEventAttributesImpactedResourcesItem],),
            "new_value": (dict,),
            "prev_value": (dict,),
            "service": (str,),
            "timestamp": (int,),
            "title": (str,),
        }

    attribute_map = {
        "aggregation_key": "aggregation_key",
        "author": "author",
        "change_metadata": "change_metadata",
        "changed_resource": "changed_resource",
        "evt": "evt",
        "impacted_resources": "impacted_resources",
        "new_value": "new_value",
        "prev_value": "prev_value",
        "service": "service",
        "timestamp": "timestamp",
        "title": "title",
    }

    def __init__(
        self_,
        aggregation_key: Union[str, UnsetType] = unset,
        author: Union[ChangeEventAttributesAuthor, UnsetType] = unset,
        change_metadata: Union[dict, UnsetType] = unset,
        changed_resource: Union[ChangeEventAttributesChangedResource, UnsetType] = unset,
        evt: Union[EventSystemAttributes, UnsetType] = unset,
        impacted_resources: Union[List[ChangeEventAttributesImpactedResourcesItem], UnsetType] = unset,
        new_value: Union[dict, UnsetType] = unset,
        prev_value: Union[dict, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        timestamp: Union[int, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Change event attributes.

        :param aggregation_key: Aggregation key of the event.
        :type aggregation_key: str, optional

        :param author: The entity that made the change.
        :type author: ChangeEventAttributesAuthor, optional

        :param change_metadata: JSON object of change metadata.
        :type change_metadata: dict, optional

        :param changed_resource: A uniquely identified resource.
        :type changed_resource: ChangeEventAttributesChangedResource, optional

        :param evt: JSON object of event system attributes.
        :type evt: EventSystemAttributes, optional

        :param impacted_resources: A list of resources impacted by this change.
        :type impacted_resources: [ChangeEventAttributesImpactedResourcesItem], optional

        :param new_value: The new state of the changed resource.
        :type new_value: dict, optional

        :param prev_value: The previous state of the changed resource.
        :type prev_value: dict, optional

        :param service: Service that triggered the event.
        :type service: str, optional

        :param timestamp: POSIX timestamp of the event.
        :type timestamp: int, optional

        :param title: The title of the event.
        :type title: str, optional
        """
        if aggregation_key is not unset:
            kwargs["aggregation_key"] = aggregation_key
        if author is not unset:
            kwargs["author"] = author
        if change_metadata is not unset:
            kwargs["change_metadata"] = change_metadata
        if changed_resource is not unset:
            kwargs["changed_resource"] = changed_resource
        if evt is not unset:
            kwargs["evt"] = evt
        if impacted_resources is not unset:
            kwargs["impacted_resources"] = impacted_resources
        if new_value is not unset:
            kwargs["new_value"] = new_value
        if prev_value is not unset:
            kwargs["prev_value"] = prev_value
        if service is not unset:
            kwargs["service"] = service
        if timestamp is not unset:
            kwargs["timestamp"] = timestamp
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)
