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
    from datadog_api_client.v2.model.tenancy_config_data_attributes_logs_config import (
        TenancyConfigDataAttributesLogsConfig,
    )
    from datadog_api_client.v2.model.tenancy_config_data_attributes_metrics_config import (
        TenancyConfigDataAttributesMetricsConfig,
    )
    from datadog_api_client.v2.model.tenancy_config_data_attributes_regions_config import (
        TenancyConfigDataAttributesRegionsConfig,
    )


class TenancyConfigDataAttributes(ModelNormal):
    validations = {
        "billing_plan_id": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tenancy_config_data_attributes_logs_config import (
            TenancyConfigDataAttributesLogsConfig,
        )
        from datadog_api_client.v2.model.tenancy_config_data_attributes_metrics_config import (
            TenancyConfigDataAttributesMetricsConfig,
        )
        from datadog_api_client.v2.model.tenancy_config_data_attributes_regions_config import (
            TenancyConfigDataAttributesRegionsConfig,
        )

        return {
            "billing_plan_id": (int,),
            "config_version": (int,),
            "cost_collection_enabled": (bool,),
            "dd_compartment_id": (str,),
            "dd_stack_id": (str,),
            "home_region": (str,),
            "logs_config": (TenancyConfigDataAttributesLogsConfig,),
            "metrics_config": (TenancyConfigDataAttributesMetricsConfig,),
            "parent_tenancy_name": (str,),
            "regions_config": (TenancyConfigDataAttributesRegionsConfig,),
            "resource_collection_enabled": (bool,),
            "tenancy_name": (str,),
            "user_ocid": (str,),
        }

    attribute_map = {
        "billing_plan_id": "billing_plan_id",
        "config_version": "config_version",
        "cost_collection_enabled": "cost_collection_enabled",
        "dd_compartment_id": "dd_compartment_id",
        "dd_stack_id": "dd_stack_id",
        "home_region": "home_region",
        "logs_config": "logs_config",
        "metrics_config": "metrics_config",
        "parent_tenancy_name": "parent_tenancy_name",
        "regions_config": "regions_config",
        "resource_collection_enabled": "resource_collection_enabled",
        "tenancy_name": "tenancy_name",
        "user_ocid": "user_ocid",
    }

    def __init__(
        self_,
        billing_plan_id: Union[int, UnsetType] = unset,
        config_version: Union[int, UnsetType] = unset,
        cost_collection_enabled: Union[bool, UnsetType] = unset,
        dd_compartment_id: Union[str, UnsetType] = unset,
        dd_stack_id: Union[str, UnsetType] = unset,
        home_region: Union[str, UnsetType] = unset,
        logs_config: Union[TenancyConfigDataAttributesLogsConfig, UnsetType] = unset,
        metrics_config: Union[TenancyConfigDataAttributesMetricsConfig, UnsetType] = unset,
        parent_tenancy_name: Union[str, UnsetType] = unset,
        regions_config: Union[TenancyConfigDataAttributesRegionsConfig, UnsetType] = unset,
        resource_collection_enabled: Union[bool, UnsetType] = unset,
        tenancy_name: Union[str, UnsetType] = unset,
        user_ocid: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param billing_plan_id:
        :type billing_plan_id: int, optional

        :param config_version:
        :type config_version: int, optional

        :param cost_collection_enabled:
        :type cost_collection_enabled: bool, optional

        :param dd_compartment_id:
        :type dd_compartment_id: str, optional

        :param dd_stack_id:
        :type dd_stack_id: str, optional

        :param home_region:
        :type home_region: str, optional

        :param logs_config:
        :type logs_config: TenancyConfigDataAttributesLogsConfig, optional

        :param metrics_config:
        :type metrics_config: TenancyConfigDataAttributesMetricsConfig, optional

        :param parent_tenancy_name:
        :type parent_tenancy_name: str, optional

        :param regions_config:
        :type regions_config: TenancyConfigDataAttributesRegionsConfig, optional

        :param resource_collection_enabled:
        :type resource_collection_enabled: bool, optional

        :param tenancy_name:
        :type tenancy_name: str, optional

        :param user_ocid:
        :type user_ocid: str, optional
        """
        if billing_plan_id is not unset:
            kwargs["billing_plan_id"] = billing_plan_id
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
        if parent_tenancy_name is not unset:
            kwargs["parent_tenancy_name"] = parent_tenancy_name
        if regions_config is not unset:
            kwargs["regions_config"] = regions_config
        if resource_collection_enabled is not unset:
            kwargs["resource_collection_enabled"] = resource_collection_enabled
        if tenancy_name is not unset:
            kwargs["tenancy_name"] = tenancy_name
        if user_ocid is not unset:
            kwargs["user_ocid"] = user_ocid
        super().__init__(kwargs)
