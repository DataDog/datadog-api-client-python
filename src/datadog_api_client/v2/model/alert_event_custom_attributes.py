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
    from datadog_api_client.v2.model.alert_event_custom_attributes_custom import AlertEventCustomAttributesCustom
    from datadog_api_client.v2.model.alert_event_custom_attributes_links_items import (
        AlertEventCustomAttributesLinksItems,
    )
    from datadog_api_client.v2.model.alert_event_custom_attributes_priority import AlertEventCustomAttributesPriority
    from datadog_api_client.v2.model.alert_event_custom_attributes_status import AlertEventCustomAttributesStatus


class AlertEventCustomAttributes(ModelNormal):
    validations = {
        "links": {
            "max_items": 20,
            "min_items": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.alert_event_custom_attributes_custom import AlertEventCustomAttributesCustom
        from datadog_api_client.v2.model.alert_event_custom_attributes_links_items import (
            AlertEventCustomAttributesLinksItems,
        )
        from datadog_api_client.v2.model.alert_event_custom_attributes_priority import (
            AlertEventCustomAttributesPriority,
        )
        from datadog_api_client.v2.model.alert_event_custom_attributes_status import AlertEventCustomAttributesStatus

        return {
            "custom": (AlertEventCustomAttributesCustom,),
            "links": ([AlertEventCustomAttributesLinksItems],),
            "priority": (AlertEventCustomAttributesPriority,),
            "status": (AlertEventCustomAttributesStatus,),
        }

    attribute_map = {
        "custom": "custom",
        "links": "links",
        "priority": "priority",
        "status": "status",
    }

    def __init__(
        self_,
        status: AlertEventCustomAttributesStatus,
        custom: Union[AlertEventCustomAttributesCustom, UnsetType] = unset,
        links: Union[List[AlertEventCustomAttributesLinksItems], UnsetType] = unset,
        priority: Union[AlertEventCustomAttributesPriority, UnsetType] = unset,
        **kwargs,
    ):
        """
        Alert event attributes.

        :param custom: Free form JSON object for arbitrary data. Supports up to 100 properties per object and a maximum nesting depth of 10 levels.
        :type custom: AlertEventCustomAttributesCustom, optional

        :param links: The links related to the event. Maximum of 20 links allowed.
        :type links: [AlertEventCustomAttributesLinksItems], optional

        :param priority: The priority of the alert.
        :type priority: AlertEventCustomAttributesPriority, optional

        :param status: The status of the alert.
        :type status: AlertEventCustomAttributesStatus
        """
        if custom is not unset:
            kwargs["custom"] = custom
        if links is not unset:
            kwargs["links"] = links
        if priority is not unset:
            kwargs["priority"] = priority
        super().__init__(kwargs)

        self_.status = status
