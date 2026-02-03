# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_tenancy_config_data_attributes_auth_credentials import (
        CreateTenancyConfigDataAttributesAuthCredentials,
    )
    from datadog_api_client.v2.model.create_tenancy_config_data_attributes_logs_config import (
        CreateTenancyConfigDataAttributesLogsConfig,
    )
    from datadog_api_client.v2.model.create_tenancy_config_data_attributes_metrics_config import (
        CreateTenancyConfigDataAttributesMetricsConfig,
    )
    from datadog_api_client.v2.model.create_tenancy_config_data_attributes_regions_config import (
        CreateTenancyConfigDataAttributesRegionsConfig,
    )


class CreateTenancyConfigDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_tenancy_config_data_attributes_auth_credentials import (
            CreateTenancyConfigDataAttributesAuthCredentials,
        )
        from datadog_api_client.v2.model.create_tenancy_config_data_attributes_logs_config import (
            CreateTenancyConfigDataAttributesLogsConfig,
        )
        from datadog_api_client.v2.model.create_tenancy_config_data_attributes_metrics_config import (
            CreateTenancyConfigDataAttributesMetricsConfig,
        )
        from datadog_api_client.v2.model.create_tenancy_config_data_attributes_regions_config import (
            CreateTenancyConfigDataAttributesRegionsConfig,
        )

        return {
            "auth_credentials": (CreateTenancyConfigDataAttributesAuthCredentials,),
            "config_version": (int, none_type),
            "cost_collection_enabled": (bool,),
            "dd_compartment_id": (str,),
            "dd_stack_id": (str,),
            "home_region": (str,),
            "logs_config": (CreateTenancyConfigDataAttributesLogsConfig,),
            "metrics_config": (CreateTenancyConfigDataAttributesMetricsConfig,),
            "regions_config": (CreateTenancyConfigDataAttributesRegionsConfig,),
            "resource_collection_enabled": (bool,),
            "user_ocid": (str,),
        }

    attribute_map = {
        "auth_credentials": "auth_credentials",
        "config_version": "config_version",
        "cost_collection_enabled": "cost_collection_enabled",
        "dd_compartment_id": "dd_compartment_id",
        "dd_stack_id": "dd_stack_id",
        "home_region": "home_region",
        "logs_config": "logs_config",
        "metrics_config": "metrics_config",
        "regions_config": "regions_config",
        "resource_collection_enabled": "resource_collection_enabled",
        "user_ocid": "user_ocid",
    }

    def __init__(
        self_,
        auth_credentials: CreateTenancyConfigDataAttributesAuthCredentials,
        home_region: str,
        user_ocid: str,
        config_version: Union[int, none_type, UnsetType] = unset,
        cost_collection_enabled: Union[bool, UnsetType] = unset,
        dd_compartment_id: Union[str, UnsetType] = unset,
        dd_stack_id: Union[str, UnsetType] = unset,
        logs_config: Union[CreateTenancyConfigDataAttributesLogsConfig, UnsetType] = unset,
        metrics_config: Union[CreateTenancyConfigDataAttributesMetricsConfig, UnsetType] = unset,
        regions_config: Union[CreateTenancyConfigDataAttributesRegionsConfig, UnsetType] = unset,
        resource_collection_enabled: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param auth_credentials:
        :type auth_credentials: CreateTenancyConfigDataAttributesAuthCredentials

        :param config_version:
        :type config_version: int, none_type, optional

        :param cost_collection_enabled:
        :type cost_collection_enabled: bool, optional

        :param dd_compartment_id:
        :type dd_compartment_id: str, optional

        :param dd_stack_id:
        :type dd_stack_id: str, optional

        :param home_region:
        :type home_region: str

        :param logs_config:
        :type logs_config: CreateTenancyConfigDataAttributesLogsConfig, optional

        :param metrics_config:
        :type metrics_config: CreateTenancyConfigDataAttributesMetricsConfig, optional

        :param regions_config:
        :type regions_config: CreateTenancyConfigDataAttributesRegionsConfig, optional

        :param resource_collection_enabled:
        :type resource_collection_enabled: bool, optional

        :param user_ocid:
        :type user_ocid: str
        """
        if config_version is not unset:
            kwargs["config_version"] = config_version
        if cost_collection_enabled is not unset:
            kwargs["cost_collection_enabled"] = cost_collection_enabled
        if dd_compartment_id is not unset:
            kwargs["dd_compartment_id"] = dd_compartment_id
        if dd_stack_id is not unset:
            kwargs["dd_stack_id"] = dd_stack_id
        if logs_config is not unset:
            kwargs["logs_config"] = logs_config
        if metrics_config is not unset:
            kwargs["metrics_config"] = metrics_config
        if regions_config is not unset:
            kwargs["regions_config"] = regions_config
        if resource_collection_enabled is not unset:
            kwargs["resource_collection_enabled"] = resource_collection_enabled
        super().__init__(kwargs)

        self_.auth_credentials = auth_credentials
        self_.home_region = home_region
        self_.user_ocid = user_ocid
