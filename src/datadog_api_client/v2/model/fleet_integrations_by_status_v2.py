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
    from datadog_api_client.v2.model.fleet_configuration_file_v2 import FleetConfigurationFileV2
    from datadog_api_client.v2.model.fleet_integration_details_v2 import FleetIntegrationDetailsV2
    from datadog_api_client.v2.model.fleet_detected_integration import FleetDetectedIntegration


class FleetIntegrationsByStatusV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fleet_configuration_file_v2 import FleetConfigurationFileV2
        from datadog_api_client.v2.model.fleet_integration_details_v2 import FleetIntegrationDetailsV2
        from datadog_api_client.v2.model.fleet_detected_integration import FleetDetectedIntegration

        return {
            "cluster_name": (str,),
            "configuration_files": ([FleetConfigurationFileV2],),
            "datadog_agent_key": (str,),
            "error_integrations": ([FleetIntegrationDetailsV2],),
            "k8s_cluster_key": (str,),
            "missing_integrations": ([FleetDetectedIntegration],),
            "warning_integrations": ([FleetIntegrationDetailsV2],),
            "working_integrations": ([FleetIntegrationDetailsV2],),
        }

    attribute_map = {
        "cluster_name": "cluster_name",
        "configuration_files": "configuration_files",
        "datadog_agent_key": "datadog_agent_key",
        "error_integrations": "error_integrations",
        "k8s_cluster_key": "k8s_cluster_key",
        "missing_integrations": "missing_integrations",
        "warning_integrations": "warning_integrations",
        "working_integrations": "working_integrations",
    }

    def __init__(
        self_,
        cluster_name: Union[str, UnsetType] = unset,
        configuration_files: Union[List[FleetConfigurationFileV2], UnsetType] = unset,
        datadog_agent_key: Union[str, UnsetType] = unset,
        error_integrations: Union[List[FleetIntegrationDetailsV2], UnsetType] = unset,
        k8s_cluster_key: Union[str, UnsetType] = unset,
        missing_integrations: Union[List[FleetDetectedIntegration], UnsetType] = unset,
        warning_integrations: Union[List[FleetIntegrationDetailsV2], UnsetType] = unset,
        working_integrations: Union[List[FleetIntegrationDetailsV2], UnsetType] = unset,
        **kwargs,
    ):
        """
        Integrations organized by their status.

        :param cluster_name: The Kubernetes cluster name, if the agent runs in a cluster.
        :type cluster_name: str, optional

        :param configuration_files: Configuration files for integrations.
        :type configuration_files: [FleetConfigurationFileV2], optional

        :param datadog_agent_key: The unique agent key identifier.
        :type datadog_agent_key: str, optional

        :param error_integrations: Integrations with errors.
        :type error_integrations: [FleetIntegrationDetailsV2], optional

        :param k8s_cluster_key: The Kubernetes cluster key, if the agent runs in a cluster.
        :type k8s_cluster_key: str, optional

        :param missing_integrations: Detected but not configured integrations.
        :type missing_integrations: [FleetDetectedIntegration], optional

        :param warning_integrations: Integrations with warnings.
        :type warning_integrations: [FleetIntegrationDetailsV2], optional

        :param working_integrations: Integrations that are working correctly.
        :type working_integrations: [FleetIntegrationDetailsV2], optional
        """
        if cluster_name is not unset:
            kwargs["cluster_name"] = cluster_name
        if configuration_files is not unset:
            kwargs["configuration_files"] = configuration_files
        if datadog_agent_key is not unset:
            kwargs["datadog_agent_key"] = datadog_agent_key
        if error_integrations is not unset:
            kwargs["error_integrations"] = error_integrations
        if k8s_cluster_key is not unset:
            kwargs["k8s_cluster_key"] = k8s_cluster_key
        if missing_integrations is not unset:
            kwargs["missing_integrations"] = missing_integrations
        if warning_integrations is not unset:
            kwargs["warning_integrations"] = warning_integrations
        if working_integrations is not unset:
            kwargs["working_integrations"] = working_integrations
        super().__init__(kwargs)
