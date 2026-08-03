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
    from datadog_api_client.v2.model.fleet_configuration_layer import FleetConfigurationLayer
    from datadog_api_client.v2.model.fleet_otel_collector_configuration_v2 import FleetOtelCollectorConfigurationV2


class FleetAgentConfigurationFilesV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_configuration_layer import FleetConfigurationLayer
        from datadog_api_client.v2.model.fleet_otel_collector_configuration_v2 import FleetOtelCollectorConfigurationV2

        return {
            "agent_configuration": (FleetConfigurationLayer,),
            "application_monitoring_configuration": (FleetConfigurationLayer,),
            "datadog_agent_key": (str,),
            "otel_collectors_configuration": ([FleetOtelCollectorConfigurationV2],),
            "security_agent_configuration": (FleetConfigurationLayer,),
            "system_probe_configuration": (FleetConfigurationLayer,),
            "version": (str,),
        }

    attribute_map = {
        "agent_configuration": "agent_configuration",
        "application_monitoring_configuration": "application_monitoring_configuration",
        "datadog_agent_key": "datadog_agent_key",
        "otel_collectors_configuration": "otel_collectors_configuration",
        "security_agent_configuration": "security_agent_configuration",
        "system_probe_configuration": "system_probe_configuration",
        "version": "version",
    }

    def __init__(
        self_,
        agent_configuration: Union[FleetConfigurationLayer, UnsetType] = unset,
        application_monitoring_configuration: Union[FleetConfigurationLayer, UnsetType] = unset,
        datadog_agent_key: Union[str, UnsetType] = unset,
        otel_collectors_configuration: Union[List[FleetOtelCollectorConfigurationV2], UnsetType] = unset,
        security_agent_configuration: Union[FleetConfigurationLayer, UnsetType] = unset,
        system_probe_configuration: Union[FleetConfigurationLayer, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration details for an agent, organized by configuration layer.

        :param agent_configuration: Configuration information organized by layers.
        :type agent_configuration: FleetConfigurationLayer, optional

        :param application_monitoring_configuration: Configuration information organized by layers.
        :type application_monitoring_configuration: FleetConfigurationLayer, optional

        :param datadog_agent_key: The unique agent key identifier.
        :type datadog_agent_key: str, optional

        :param otel_collectors_configuration: Configuration for OpenTelemetry collectors associated with the agent. Present only when the agent has associated OpenTelemetry collectors.
        :type otel_collectors_configuration: [FleetOtelCollectorConfigurationV2], optional

        :param security_agent_configuration: Configuration information organized by layers.
        :type security_agent_configuration: FleetConfigurationLayer, optional

        :param system_probe_configuration: Configuration information organized by layers.
        :type system_probe_configuration: FleetConfigurationLayer, optional

        :param version: The configuration version.
        :type version: str, optional
        """
        if agent_configuration is not unset:
            kwargs["agent_configuration"] = agent_configuration
        if application_monitoring_configuration is not unset:
            kwargs["application_monitoring_configuration"] = application_monitoring_configuration
        if datadog_agent_key is not unset:
            kwargs["datadog_agent_key"] = datadog_agent_key
        if otel_collectors_configuration is not unset:
            kwargs["otel_collectors_configuration"] = otel_collectors_configuration
        if security_agent_configuration is not unset:
            kwargs["security_agent_configuration"] = security_agent_configuration
        if system_probe_configuration is not unset:
            kwargs["system_probe_configuration"] = system_probe_configuration
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
