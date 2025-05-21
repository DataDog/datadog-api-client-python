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
    from datadog_api_client.v2.model.oci_logs_config import OCILogsConfig
    from datadog_api_client.v2.model.oci_metrics_config import OCIMetricsConfig
    from datadog_api_client.v2.model.regions_config import RegionsConfig


class TenancyConfigDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.oci_logs_config import OCILogsConfig
        from datadog_api_client.v2.model.oci_metrics_config import OCIMetricsConfig
        from datadog_api_client.v2.model.regions_config import RegionsConfig

        return {
            "config_version": (int,),
            "cost_collection_enabled": (bool,),
            "dd_compartment_id": (str,),
            "dd_stack_id": (str,),
            "home_region": (str,),
            "logs_config": (OCILogsConfig,),
            "metrics_config": (OCIMetricsConfig,),
            "regions_config": (RegionsConfig,),
            "resource_collection_enabled": (bool,),
            "tenancy_name": (str,),
            "user_ocid": (str,),
        }

    attribute_map = {
        "config_version": "config_version",
        "cost_collection_enabled": "cost_collection_enabled",
        "dd_compartment_id": "dd_compartment_id",
        "dd_stack_id": "dd_stack_id",
        "home_region": "home_region",
        "logs_config": "logs_config",
        "metrics_config": "metrics_config",
        "regions_config": "regions_config",
        "resource_collection_enabled": "resource_collection_enabled",
        "tenancy_name": "tenancy_name",
        "user_ocid": "user_ocid",
    }

    def __init__(
        self_,
        config_version: Union[int, UnsetType] = unset,
        cost_collection_enabled: Union[bool, UnsetType] = unset,
        dd_compartment_id: Union[str, UnsetType] = unset,
        dd_stack_id: Union[str, UnsetType] = unset,
        home_region: Union[str, UnsetType] = unset,
        logs_config: Union[OCILogsConfig, UnsetType] = unset,
        metrics_config: Union[OCIMetricsConfig, UnsetType] = unset,
        regions_config: Union[RegionsConfig, UnsetType] = unset,
        resource_collection_enabled: Union[bool, UnsetType] = unset,
        tenancy_name: Union[str, UnsetType] = unset,
        user_ocid: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``TenancyConfigDataAttributes`` object.

        :param config_version: The config version. It is not recommended to add or change this value, as it is determined internally.
        :type config_version: int, optional

        :param cost_collection_enabled: Enable or disable cost collection.
        :type cost_collection_enabled: bool, optional

        :param dd_compartment_id: The OCID of the compartment containing Datadog managed resources.
        :type dd_compartment_id: str, optional

        :param dd_stack_id: The OCID of the resource manager stack for creating Datadog managed resources.
        :type dd_stack_id: str, optional

        :param home_region: The home region of the tenancy to be integrated.
        :type home_region: str, optional

        :param logs_config: The definition of ``OCILogsConfig`` object.
        :type logs_config: OCILogsConfig, optional

        :param metrics_config: The definition of ``OCIMetricsConfig`` object.
        :type metrics_config: OCIMetricsConfig, optional

        :param regions_config: The definition of ``RegionsConfig`` object.
        :type regions_config: RegionsConfig, optional

        :param resource_collection_enabled: Enable or disable resource collection.
        :type resource_collection_enabled: bool, optional

        :param tenancy_name: The attribute's tenancy_name.
        :type tenancy_name: str, optional

        :param user_ocid: The OCID of the user needed to authenticate and collect data.
        :type user_ocid: str, optional
        """
        if config_version is not unset:
            kwargs["config_version"] = config_version
        if cost_collection_enabled is not unset:
            kwargs["cost_collection_enabled"] = cost_collection_enabled
        if dd_compartment_id is not unset:
            kwargs["dd_compartment_id"] = dd_compartment_id
        if dd_stack_id is not unset:
            kwargs["dd_stack_id"] = dd_stack_id
        if home_region is not unset:
            kwargs["home_region"] = home_region
        if logs_config is not unset:
            kwargs["logs_config"] = logs_config
        if metrics_config is not unset:
            kwargs["metrics_config"] = metrics_config
        if regions_config is not unset:
            kwargs["regions_config"] = regions_config
        if resource_collection_enabled is not unset:
            kwargs["resource_collection_enabled"] = resource_collection_enabled
        if tenancy_name is not unset:
            kwargs["tenancy_name"] = tenancy_name
        if user_ocid is not unset:
            kwargs["user_ocid"] = user_ocid
        super().__init__(kwargs)
