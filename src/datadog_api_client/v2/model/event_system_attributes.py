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
    from datadog_api_client.v2.model.event_system_attributes_category import EventSystemAttributesCategory
    from datadog_api_client.v2.model.event_system_attributes_integration_id import EventSystemAttributesIntegrationId


class EventSystemAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_system_attributes_category import EventSystemAttributesCategory
        from datadog_api_client.v2.model.event_system_attributes_integration_id import (
            EventSystemAttributesIntegrationId,
        )

        return {
            "category": (EventSystemAttributesCategory,),
            "id": (str,),
            "integration_id": (EventSystemAttributesIntegrationId,),
            "source_id": (int,),
            "uid": (str,),
        }

    attribute_map = {
        "category": "category",
        "id": "id",
        "integration_id": "integration_id",
        "source_id": "source_id",
        "uid": "uid",
    }

    def __init__(
        self_,
        category: Union[EventSystemAttributesCategory, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        integration_id: Union[EventSystemAttributesIntegrationId, UnsetType] = unset,
        source_id: Union[int, UnsetType] = unset,
        uid: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON object of event system attributes.

        :param category: Event category identifying the type of event.
        :type category: EventSystemAttributesCategory, optional

        :param id: Event identifier. This field is deprecated and will be removed in a future version. Use the ``uid`` field instead.
        :type id: str, optional

        :param integration_id: Integration ID sourced from integration manifests.
        :type integration_id: EventSystemAttributesIntegrationId, optional

        :param source_id: The source type ID of the event.
        :type source_id: int, optional

        :param uid: A unique identifier for the event. You can use this identifier to query or reference the event.
        :type uid: str, optional
        """
        if category is not unset:
            kwargs["category"] = category
        if id is not unset:
            kwargs["id"] = id
        if integration_id is not unset:
            kwargs["integration_id"] = integration_id
        if source_id is not unset:
            kwargs["source_id"] = source_id
        if uid is not unset:
            kwargs["uid"] = uid
        super().__init__(kwargs)
