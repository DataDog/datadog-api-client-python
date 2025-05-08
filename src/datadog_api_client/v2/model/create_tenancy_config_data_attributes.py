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
    from datadog_api_client.v2.model.auth_credentials import AuthCredentials
    from datadog_api_client.v2.model.oci_logs_config import OCILogsConfig
    from datadog_api_client.v2.model.oci_metrics_config import OCIMetricsConfig


class CreateTenancyConfigDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.auth_credentials import AuthCredentials
        from datadog_api_client.v2.model.oci_logs_config import OCILogsConfig
        from datadog_api_client.v2.model.oci_metrics_config import OCIMetricsConfig

        return {
            "auth_credentials": (AuthCredentials,),
            "config_version": (int,),
            "home_region": (str,),
            "logs_config": (OCILogsConfig,),
            "metrics_config": (OCIMetricsConfig,),
            "resource_collection_enabled": (bool,),
            "user_ocid": (str,),
        }

    attribute_map = {
        "auth_credentials": "auth_credentials",
        "config_version": "config_version",
        "home_region": "home_region",
        "logs_config": "logs_config",
        "metrics_config": "metrics_config",
        "resource_collection_enabled": "resource_collection_enabled",
        "user_ocid": "user_ocid",
    }

    def __init__(
        self_,
        auth_credentials: AuthCredentials,
        home_region: str,
        user_ocid: str,
        config_version: Union[int, UnsetType] = unset,
        logs_config: Union[OCILogsConfig, UnsetType] = unset,
        metrics_config: Union[OCIMetricsConfig, UnsetType] = unset,
        resource_collection_enabled: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``CreateTenancyConfigDataAttributes`` object.

        :param auth_credentials: The auth credentials of the user. Consists of a public key fingerprint and private key.
        :type auth_credentials: AuthCredentials

        :param config_version: The config version. It is not recommended to add or change this value, as it is determined internally.
        :type config_version: int, optional

        :param home_region: The home region of the tenancy to be integrated.
        :type home_region: str

        :param logs_config: The definition of ``OCILogsConfig`` object.
        :type logs_config: OCILogsConfig, optional

        :param metrics_config: The definition of ``OCIMetricsConfig`` object.
        :type metrics_config: OCIMetricsConfig, optional

        :param resource_collection_enabled: Enable or disable resource collection.
        :type resource_collection_enabled: bool, optional

        :param user_ocid: The OCID of the user needed to authenticate and collect data.
        :type user_ocid: str
        """
        if config_version is not unset:
            kwargs["config_version"] = config_version
        if logs_config is not unset:
            kwargs["logs_config"] = logs_config
        if metrics_config is not unset:
            kwargs["metrics_config"] = metrics_config
        if resource_collection_enabled is not unset:
            kwargs["resource_collection_enabled"] = resource_collection_enabled
        super().__init__(kwargs)

        self_.auth_credentials = auth_credentials
        self_.home_region = home_region
        self_.user_ocid = user_ocid
