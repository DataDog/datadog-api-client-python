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
    from datadog_api_client.v2.model.update_tenancy_config_data_attributes_auth_credentials import (
        UpdateTenancyConfigDataAttributesAuthCredentials,
    )
    from datadog_api_client.v2.model.update_tenancy_config_data_attributes_logs_config import (
        UpdateTenancyConfigDataAttributesLogsConfig,
    )
    from datadog_api_client.v2.model.update_tenancy_config_data_attributes_metrics_config import (
        UpdateTenancyConfigDataAttributesMetricsConfig,
    )
    from datadog_api_client.v2.model.update_tenancy_config_data_attributes_regions_config import (
        UpdateTenancyConfigDataAttributesRegionsConfig,
    )


class UpdateTenancyConfigDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_tenancy_config_data_attributes_auth_credentials import (
            UpdateTenancyConfigDataAttributesAuthCredentials,
        )
        from datadog_api_client.v2.model.update_tenancy_config_data_attributes_logs_config import (
            UpdateTenancyConfigDataAttributesLogsConfig,
        )
        from datadog_api_client.v2.model.update_tenancy_config_data_attributes_metrics_config import (
            UpdateTenancyConfigDataAttributesMetricsConfig,
        )
        from datadog_api_client.v2.model.update_tenancy_config_data_attributes_regions_config import (
            UpdateTenancyConfigDataAttributesRegionsConfig,
        )

        return {
            "auth_credentials": (UpdateTenancyConfigDataAttributesAuthCredentials,),
            "cost_collection_enabled": (bool,),
            "home_region": (str,),
            "logs_config": (UpdateTenancyConfigDataAttributesLogsConfig,),
            "metrics_config": (UpdateTenancyConfigDataAttributesMetricsConfig,),
            "regions_config": (UpdateTenancyConfigDataAttributesRegionsConfig,),
            "resource_collection_enabled": (bool,),
            "user_ocid": (str,),
        }

    attribute_map = {
        "auth_credentials": "auth_credentials",
        "cost_collection_enabled": "cost_collection_enabled",
        "home_region": "home_region",
        "logs_config": "logs_config",
        "metrics_config": "metrics_config",
        "regions_config": "regions_config",
        "resource_collection_enabled": "resource_collection_enabled",
        "user_ocid": "user_ocid",
    }

    def __init__(
        self_,
        auth_credentials: Union[UpdateTenancyConfigDataAttributesAuthCredentials, UnsetType] = unset,
        cost_collection_enabled: Union[bool, UnsetType] = unset,
        home_region: Union[str, UnsetType] = unset,
        logs_config: Union[UpdateTenancyConfigDataAttributesLogsConfig, UnsetType] = unset,
        metrics_config: Union[UpdateTenancyConfigDataAttributesMetricsConfig, UnsetType] = unset,
        regions_config: Union[UpdateTenancyConfigDataAttributesRegionsConfig, UnsetType] = unset,
        resource_collection_enabled: Union[bool, UnsetType] = unset,
        user_ocid: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param auth_credentials:
        :type auth_credentials: UpdateTenancyConfigDataAttributesAuthCredentials, optional

        :param cost_collection_enabled:
        :type cost_collection_enabled: bool, optional

        :param home_region:
        :type home_region: str, optional

        :param logs_config:
        :type logs_config: UpdateTenancyConfigDataAttributesLogsConfig, optional

        :param metrics_config:
        :type metrics_config: UpdateTenancyConfigDataAttributesMetricsConfig, optional

        :param regions_config:
        :type regions_config: UpdateTenancyConfigDataAttributesRegionsConfig, optional

        :param resource_collection_enabled:
        :type resource_collection_enabled: bool, optional

        :param user_ocid:
        :type user_ocid: str, optional
        """
        if auth_credentials is not unset:
            kwargs["auth_credentials"] = auth_credentials
        if cost_collection_enabled is not unset:
            kwargs["cost_collection_enabled"] = cost_collection_enabled
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
        if user_ocid is not unset:
            kwargs["user_ocid"] = user_ocid
        super().__init__(kwargs)
