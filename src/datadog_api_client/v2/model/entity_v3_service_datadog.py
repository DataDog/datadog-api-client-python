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
    from datadog_api_client.v2.model.entity_v3_datadog_code_location_item import EntityV3DatadogCodeLocationItem
    from datadog_api_client.v2.model.entity_v3_datadog_event_item import EntityV3DatadogEventItem
    from datadog_api_client.v2.model.entity_v3_datadog_log_item import EntityV3DatadogLogItem
    from datadog_api_client.v2.model.entity_v3_datadog_performance import EntityV3DatadogPerformance
    from datadog_api_client.v2.model.entity_v3_datadog_pipelines import EntityV3DatadogPipelines


class EntityV3ServiceDatadog(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_v3_datadog_code_location_item import EntityV3DatadogCodeLocationItem
        from datadog_api_client.v2.model.entity_v3_datadog_event_item import EntityV3DatadogEventItem
        from datadog_api_client.v2.model.entity_v3_datadog_log_item import EntityV3DatadogLogItem
        from datadog_api_client.v2.model.entity_v3_datadog_performance import EntityV3DatadogPerformance
        from datadog_api_client.v2.model.entity_v3_datadog_pipelines import EntityV3DatadogPipelines

        return {
            "code_locations": ([EntityV3DatadogCodeLocationItem],),
            "events": ([EntityV3DatadogEventItem],),
            "logs": ([EntityV3DatadogLogItem],),
            "performance_data": (EntityV3DatadogPerformance,),
            "pipelines": (EntityV3DatadogPipelines,),
        }

    attribute_map = {
        "code_locations": "codeLocations",
        "events": "events",
        "logs": "logs",
        "performance_data": "performanceData",
        "pipelines": "pipelines",
    }

    def __init__(
        self_,
        code_locations: Union[List[EntityV3DatadogCodeLocationItem], UnsetType] = unset,
        events: Union[List[EntityV3DatadogEventItem], UnsetType] = unset,
        logs: Union[List[EntityV3DatadogLogItem], UnsetType] = unset,
        performance_data: Union[EntityV3DatadogPerformance, UnsetType] = unset,
        pipelines: Union[EntityV3DatadogPipelines, UnsetType] = unset,
        **kwargs,
    ):
        """
        Datadog product integrations for the service entity

        :param code_locations: Schema for mapping source code locations to an entity
        :type code_locations: [EntityV3DatadogCodeLocationItem], optional

        :param events: Events associations
        :type events: [EntityV3DatadogEventItem], optional

        :param logs: Logs association
        :type logs: [EntityV3DatadogLogItem], optional

        :param performance_data: Performance stats association
        :type performance_data: EntityV3DatadogPerformance, optional

        :param pipelines: CI Pipelines association
        :type pipelines: EntityV3DatadogPipelines, optional
        """
        if code_locations is not unset:
            kwargs["code_locations"] = code_locations
        if events is not unset:
            kwargs["events"] = events
        if logs is not unset:
            kwargs["logs"] = logs
        if performance_data is not unset:
            kwargs["performance_data"] = performance_data
        if pipelines is not unset:
            kwargs["pipelines"] = pipelines
        super().__init__(kwargs)
