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
    from datadog_api_client.v2.model.monitor_notification_rule_relationships_created_by import (
        MonitorNotificationRuleRelationshipsCreatedBy,
    )


class MonitorNotificationRuleRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_notification_rule_relationships_created_by import (
            MonitorNotificationRuleRelationshipsCreatedBy,
        )

        return {
            "created_by": (MonitorNotificationRuleRelationshipsCreatedBy,),
        }

    attribute_map = {
        "created_by": "created_by",
    }

    def __init__(self_, created_by: Union[MonitorNotificationRuleRelationshipsCreatedBy, UnsetType] = unset, **kwargs):
        """
        All relationships associated with monitor notification rule.

        :param created_by: The user who created the monitor notification rule.
        :type created_by: MonitorNotificationRuleRelationshipsCreatedBy, optional
        """
        if created_by is not unset:
            kwargs["created_by"] = created_by
        super().__init__(kwargs)
