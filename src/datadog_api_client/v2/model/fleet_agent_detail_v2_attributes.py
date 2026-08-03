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
    from datadog_api_client.v2.model.fleet_agent_info_details_v2 import FleetAgentInfoDetailsV2
    from datadog_api_client.v2.model.fleet_agent_configuration_files_v2 import FleetAgentConfigurationFilesV2
    from datadog_api_client.v2.model.fleet_integrations_by_status_v2 import FleetIntegrationsByStatusV2


class FleetAgentDetailV2Attributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_agent_info_details_v2 import FleetAgentInfoDetailsV2
        from datadog_api_client.v2.model.fleet_agent_configuration_files_v2 import FleetAgentConfigurationFilesV2
        from datadog_api_client.v2.model.fleet_integrations_by_status_v2 import FleetIntegrationsByStatusV2

        return {
            "agent_infos": (FleetAgentInfoDetailsV2,),
            "configuration_files": (FleetAgentConfigurationFilesV2,),
            "integrations": (FleetIntegrationsByStatusV2,),
        }

    attribute_map = {
        "agent_infos": "agent_infos",
        "configuration_files": "configuration_files",
        "integrations": "integrations",
    }

    def __init__(
        self_,
        agent_infos: FleetAgentInfoDetailsV2,
        configuration_files: Union[FleetAgentConfigurationFilesV2, UnsetType] = unset,
        integrations: Union[FleetIntegrationsByStatusV2, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for the v2 agent detail response.

        :param agent_infos: Detailed information about a Datadog Agent.
        :type agent_infos: FleetAgentInfoDetailsV2

        :param configuration_files: Configuration details for an agent, organized by configuration layer.
        :type configuration_files: FleetAgentConfigurationFilesV2, optional

        :param integrations: Integrations organized by their status.
        :type integrations: FleetIntegrationsByStatusV2, optional
        """
        if configuration_files is not unset:
            kwargs["configuration_files"] = configuration_files
        if integrations is not unset:
            kwargs["integrations"] = integrations
        super().__init__(kwargs)

        self_.agent_infos = agent_infos
