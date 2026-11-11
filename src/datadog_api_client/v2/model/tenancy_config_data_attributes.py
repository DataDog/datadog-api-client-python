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
    from datadog_api_client.v2.model.tenancy_config_data_attributes_grace_resource import (
        TenancyConfigDataAttributesGraceResource,
    )
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
        from datadog_api_client.v2.model.tenancy_config_data_attributes_grace_resource import (
            TenancyConfigDataAttributesGraceResource,
        )
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
            "account_tags": ([str],),
            "billing_plan_id": (int,),
            "config_version": (int,),
            "cost_collection_enabled": (bool,),
            "dd_compartment_id": (str,),
            "dd_iac_version": (str,),
            "dd_stack_id": (str,),
            "defined_tags": ([str],),
            "events_collection_enabled": (bool,),
            "grace_resource": (TenancyConfigDataAttributesGraceResource,),
            "home_region": (str,),
            "logs_config": (TenancyConfigDataAttributesLogsConfig,),
            "metrics_config": (TenancyConfigDataAttributesMetricsConfig,),
            "parent_tenancy_name": (str,),
            "regions_config": (TenancyConfigDataAttributesRegionsConfig,),
            "resource_collection_enabled": (bool,),
            "service_quota_collection_enabled": (bool,),
            "tenancy_name": (str,),
            "user_ocid": (str,),
        }

    attribute_map = {
        "account_tags": "account_tags",
        "billing_plan_id": "billing_plan_id",
        "config_version": "config_version",
        "cost_collection_enabled": "cost_collection_enabled",
        "dd_compartment_id": "dd_compartment_id",
        "dd_iac_version": "dd_iac_version",
        "dd_stack_id": "dd_stack_id",
        "defined_tags": "defined_tags",
        "events_collection_enabled": "events_collection_enabled",
        "grace_resource": "grace_resource",
        "home_region": "home_region",
        "logs_config": "logs_config",
        "metrics_config": "metrics_config",
        "parent_tenancy_name": "parent_tenancy_name",
        "regions_config": "regions_config",
        "resource_collection_enabled": "resource_collection_enabled",
        "service_quota_collection_enabled": "service_quota_collection_enabled",
        "tenancy_name": "tenancy_name",
        "user_ocid": "user_ocid",
    }

    def __init__(
        self_,
        account_tags: Union[List[str], UnsetType] = unset,
        billing_plan_id: Union[int, UnsetType] = unset,
        config_version: Union[int, UnsetType] = unset,
        cost_collection_enabled: Union[bool, UnsetType] = unset,
        dd_compartment_id: Union[str, UnsetType] = unset,
        dd_iac_version: Union[str, UnsetType] = unset,
        dd_stack_id: Union[str, UnsetType] = unset,
        defined_tags: Union[List[str], UnsetType] = unset,
        events_collection_enabled: Union[bool, UnsetType] = unset,
        grace_resource: Union[TenancyConfigDataAttributesGraceResource, UnsetType] = unset,
        home_region: Union[str, UnsetType] = unset,
        logs_config: Union[TenancyConfigDataAttributesLogsConfig, UnsetType] = unset,
        metrics_config: Union[TenancyConfigDataAttributesMetricsConfig, UnsetType] = unset,
        parent_tenancy_name: Union[str, UnsetType] = unset,
        regions_config: Union[TenancyConfigDataAttributesRegionsConfig, UnsetType] = unset,
        resource_collection_enabled: Union[bool, UnsetType] = unset,
        service_quota_collection_enabled: Union[bool, UnsetType] = unset,
        tenancy_name: Union[str, UnsetType] = unset,
        user_ocid: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an OCI tenancy integration configuration, including authentication details, region settings, and collection options.

        :param account_tags: List of Datadog tags applied to data collected from the tenancy.
        :type account_tags: [str], optional

        :param billing_plan_id: The identifier of the billing plan associated with the OCI tenancy.
        :type billing_plan_id: int, optional

        :param config_version: Version number of the integration the tenancy is integrated with
        :type config_version: int, optional

        :param cost_collection_enabled: Whether cost data collection from OCI is enabled for the tenancy.
        :type cost_collection_enabled: bool, optional

        :param dd_compartment_id: The OCID of the OCI compartment used by the Datadog integration stack.
        :type dd_compartment_id: str, optional

        :param dd_iac_version: The version of the Datadog infrastructure-as-code stack applied to the tenancy (for example, 1.2.0).
        :type dd_iac_version: str, optional

        :param dd_stack_id: The OCID of the OCI Resource Manager stack used by the Datadog integration.
        :type dd_stack_id: str, optional

        :param defined_tags: List of OCI defined tags applied to the Datadog-managed connector hubs.
        :type defined_tags: [str], optional

        :param events_collection_enabled: Whether resource change events collection from OCI is enabled for the tenancy.
        :type events_collection_enabled: bool, optional

        :param grace_resource: Access control details for the tenancy configuration, used to determine whether the requesting user can edit it.
        :type grace_resource: TenancyConfigDataAttributesGraceResource, optional

        :param home_region: The home region of the OCI tenancy (for example, us-ashburn-1).
        :type home_region: str, optional

        :param logs_config: Log collection configuration for an OCI tenancy, indicating which compartments and services have log collection enabled.
        :type logs_config: TenancyConfigDataAttributesLogsConfig, optional

        :param metrics_config: Metrics collection configuration for an OCI tenancy, indicating which compartments and services are included or excluded.
        :type metrics_config: TenancyConfigDataAttributesMetricsConfig, optional

        :param parent_tenancy_name: The name of the parent OCI tenancy, if applicable.
        :type parent_tenancy_name: str, optional

        :param regions_config: Region configuration for an OCI tenancy, indicating which regions are available, enabled, or disabled for data collection.
        :type regions_config: TenancyConfigDataAttributesRegionsConfig, optional

        :param resource_collection_enabled: Whether resource collection from OCI is enabled for the tenancy.
        :type resource_collection_enabled: bool, optional

        :param service_quota_collection_enabled: Whether service quota collection from OCI is enabled for the tenancy.
        :type service_quota_collection_enabled: bool, optional

        :param tenancy_name: The human-readable name of the OCI tenancy.
        :type tenancy_name: str, optional

        :param user_ocid: The OCID of the OCI user used by the Datadog integration for authentication.
        :type user_ocid: str, optional
        """
        if account_tags is not unset:
            kwargs["account_tags"] = account_tags
        if billing_plan_id is not unset:
            kwargs["billing_plan_id"] = billing_plan_id
        if config_version is not unset:
            kwargs["config_version"] = config_version
        if cost_collection_enabled is not unset:
            kwargs["cost_collection_enabled"] = cost_collection_enabled
        if dd_compartment_id is not unset:
            kwargs["dd_compartment_id"] = dd_compartment_id
        if dd_iac_version is not unset:
            kwargs["dd_iac_version"] = dd_iac_version
        if dd_stack_id is not unset:
            kwargs["dd_stack_id"] = dd_stack_id
        if defined_tags is not unset:
            kwargs["defined_tags"] = defined_tags
        if events_collection_enabled is not unset:
            kwargs["events_collection_enabled"] = events_collection_enabled
        if grace_resource is not unset:
            kwargs["grace_resource"] = grace_resource
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
        if service_quota_collection_enabled is not unset:
            kwargs["service_quota_collection_enabled"] = service_quota_collection_enabled
        if tenancy_name is not unset:
            kwargs["tenancy_name"] = tenancy_name
        if user_ocid is not unset:
            kwargs["user_ocid"] = user_ocid
        super().__init__(kwargs)
