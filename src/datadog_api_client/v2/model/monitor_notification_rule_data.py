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
    from datadog_api_client.v2.model.monitor_notification_rule_response_attributes import (
        MonitorNotificationRuleResponseAttributes,
    )
    from datadog_api_client.v2.model.monitor_notification_rule_relationships import MonitorNotificationRuleRelationships
    from datadog_api_client.v2.model.monitor_notification_rule_resource_type import MonitorNotificationRuleResourceType


class MonitorNotificationRuleData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_notification_rule_response_attributes import (
            MonitorNotificationRuleResponseAttributes,
        )
        from datadog_api_client.v2.model.monitor_notification_rule_relationships import (
            MonitorNotificationRuleRelationships,
        )
        from datadog_api_client.v2.model.monitor_notification_rule_resource_type import (
            MonitorNotificationRuleResourceType,
        )

        return {
            "attributes": (MonitorNotificationRuleResponseAttributes,),
            "id": (str,),
            "relationships": (MonitorNotificationRuleRelationships,),
            "type": (MonitorNotificationRuleResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[MonitorNotificationRuleResponseAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[MonitorNotificationRuleRelationships, UnsetType] = unset,
        type: Union[MonitorNotificationRuleResourceType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Monitor notification rule data.

        :param attributes: Attributes of the monitor notification rule.
        :type attributes: MonitorNotificationRuleResponseAttributes, optional

        :param id: The ID of the monitor notification rule.
        :type id: str, optional

        :param relationships: All relationships associated with monitor notification rule.
        :type relationships: MonitorNotificationRuleRelationships, optional

        :param type: Monitor notification rule resource type.
        :type type: MonitorNotificationRuleResourceType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
