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
    from datadog_api_client.v2.model.entity_v3_datadog_event_item import EntityV3DatadogEventItem
    from datadog_api_client.v2.model.entity_v3_datadog_log_item import EntityV3DatadogLogItem
    from datadog_api_client.v2.model.entity_v3_datadog_performance import EntityV3DatadogPerformance


class EntityV3QueueDatadog(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_v3_datadog_event_item import EntityV3DatadogEventItem
        from datadog_api_client.v2.model.entity_v3_datadog_log_item import EntityV3DatadogLogItem
        from datadog_api_client.v2.model.entity_v3_datadog_performance import EntityV3DatadogPerformance

        return {
            "events": ([EntityV3DatadogEventItem],),
            "logs": ([EntityV3DatadogLogItem],),
            "performance_data": (EntityV3DatadogPerformance,),
        }

    attribute_map = {
        "events": "events",
        "logs": "logs",
        "performance_data": "performanceData",
    }

    def __init__(
        self_,
        events: Union[List[EntityV3DatadogEventItem], UnsetType] = unset,
        logs: Union[List[EntityV3DatadogLogItem], UnsetType] = unset,
        performance_data: Union[EntityV3DatadogPerformance, UnsetType] = unset,
        **kwargs,
    ):
        """
        Datadog product integrations for the datastore entity

        :param events: Events associations
        :type events: [EntityV3DatadogEventItem], optional

        :param logs: Logs association
        :type logs: [EntityV3DatadogLogItem], optional

        :param performance_data: Performance stats association
        :type performance_data: EntityV3DatadogPerformance, optional
        """
        if events is not unset:
            kwargs["events"] = events
        if logs is not unset:
            kwargs["logs"] = logs
        if performance_data is not unset:
            kwargs["performance_data"] = performance_data
        super().__init__(kwargs)