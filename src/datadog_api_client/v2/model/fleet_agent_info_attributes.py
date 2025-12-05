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
    from datadog_api_client.v2.model.fleet_agent_info_details import FleetAgentInfoDetails
    from datadog_api_client.v2.model.fleet_configuration_layer import FleetConfigurationLayer
    from datadog_api_client.v2.model.fleet_detected_integration import FleetDetectedIntegration
    from datadog_api_client.v2.model.fleet_integrations_by_status import FleetIntegrationsByStatus


class FleetAgentInfoAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_agent_info_details import FleetAgentInfoDetails
        from datadog_api_client.v2.model.fleet_configuration_layer import FleetConfigurationLayer
        from datadog_api_client.v2.model.fleet_detected_integration import FleetDetectedIntegration
        from datadog_api_client.v2.model.fleet_integrations_by_status import FleetIntegrationsByStatus

        return {
            "agent_infos": (FleetAgentInfoDetails,),
            "configuration_files": (FleetConfigurationLayer,),
            "detected_integrations": ([FleetDetectedIntegration],),
            "integrations": (FleetIntegrationsByStatus,),
        }

    attribute_map = {
        "agent_infos": "agent_infos",
        "configuration_files": "configuration_files",
        "detected_integrations": "detected_integrations",
        "integrations": "integrations",
    }

    def __init__(
        self_,
        agent_infos: Union[FleetAgentInfoDetails, UnsetType] = unset,
        configuration_files: Union[FleetConfigurationLayer, UnsetType] = unset,
        detected_integrations: Union[List[FleetDetectedIntegration], UnsetType] = unset,
        integrations: Union[FleetIntegrationsByStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for agent information.

        :param agent_infos: Detailed information about a Datadog Agent.
        :type agent_infos: FleetAgentInfoDetails, optional

        :param configuration_files: Configuration information organized by layers.
        :type configuration_files: FleetConfigurationLayer, optional

        :param detected_integrations: List of detected integrations.
        :type detected_integrations: [FleetDetectedIntegration], optional

        :param integrations: Integrations organized by their status.
        :type integrations: FleetIntegrationsByStatus, optional
        """
        if agent_infos is not unset:
            kwargs["agent_infos"] = agent_infos
        if configuration_files is not unset:
            kwargs["configuration_files"] = configuration_files
        if detected_integrations is not unset:
            kwargs["detected_integrations"] = detected_integrations
        if integrations is not unset:
            kwargs["integrations"] = integrations
        super().__init__(kwargs)
