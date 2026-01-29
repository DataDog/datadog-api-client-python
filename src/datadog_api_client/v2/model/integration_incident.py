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
    from datadog_api_client.v2.model.integration_incident_field_mappings_items import (
        IntegrationIncidentFieldMappingsItems,
    )
    from datadog_api_client.v2.model.integration_incident_severity_config import IntegrationIncidentSeverityConfig


class IntegrationIncident(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.integration_incident_field_mappings_items import (
            IntegrationIncidentFieldMappingsItems,
        )
        from datadog_api_client.v2.model.integration_incident_severity_config import IntegrationIncidentSeverityConfig

        return {
            "auto_escalation_query": (str,),
            "default_incident_commander": (str,),
            "enabled": (bool,),
            "field_mappings": ([IntegrationIncidentFieldMappingsItems],),
            "incident_type": (str,),
            "severity_config": (IntegrationIncidentSeverityConfig,),
        }

    attribute_map = {
        "auto_escalation_query": "auto_escalation_query",
        "default_incident_commander": "default_incident_commander",
        "enabled": "enabled",
        "field_mappings": "field_mappings",
        "incident_type": "incident_type",
        "severity_config": "severity_config",
    }

    def __init__(
        self_,
        auto_escalation_query: Union[str, UnsetType] = unset,
        default_incident_commander: Union[str, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        field_mappings: Union[List[IntegrationIncidentFieldMappingsItems], UnsetType] = unset,
        incident_type: Union[str, UnsetType] = unset,
        severity_config: Union[IntegrationIncidentSeverityConfig, UnsetType] = unset,
        **kwargs,
    ):
        """
        Incident integration settings

        :param auto_escalation_query: Query for auto-escalation
        :type auto_escalation_query: str, optional

        :param default_incident_commander: Default incident commander
        :type default_incident_commander: str, optional

        :param enabled: Whether incident integration is enabled
        :type enabled: bool, optional

        :param field_mappings:
        :type field_mappings: [IntegrationIncidentFieldMappingsItems], optional

        :param incident_type: Incident type
        :type incident_type: str, optional

        :param severity_config:
        :type severity_config: IntegrationIncidentSeverityConfig, optional
        """
        if auto_escalation_query is not unset:
            kwargs["auto_escalation_query"] = auto_escalation_query
        if default_incident_commander is not unset:
            kwargs["default_incident_commander"] = default_incident_commander
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if field_mappings is not unset:
            kwargs["field_mappings"] = field_mappings
        if incident_type is not unset:
            kwargs["incident_type"] = incident_type
        if severity_config is not unset:
            kwargs["severity_config"] = severity_config
        super().__init__(kwargs)
