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
    from datadog_api_client.v2.model.regions_config import RegionsConfig


class UpdateTenancyConfigDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.auth_credentials import AuthCredentials
        from datadog_api_client.v2.model.oci_logs_config import OCILogsConfig
        from datadog_api_client.v2.model.oci_metrics_config import OCIMetricsConfig
        from datadog_api_client.v2.model.regions_config import RegionsConfig

        return {
            "auth_credentials": (AuthCredentials,),
            "home_region": (str,),
            "logs_config": (OCILogsConfig,),
            "metrics_config": (OCIMetricsConfig,),
            "regions_config": (RegionsConfig,),
            "resource_collection_enabled": (bool,),
            "user_ocid": (str,),
        }

    attribute_map = {
        "auth_credentials": "auth_credentials",
        "home_region": "home_region",
        "logs_config": "logs_config",
        "metrics_config": "metrics_config",
        "regions_config": "regions_config",
        "resource_collection_enabled": "resource_collection_enabled",
        "user_ocid": "user_ocid",
    }

    def __init__(
        self_,
        auth_credentials: Union[AuthCredentials, UnsetType] = unset,
        home_region: Union[str, UnsetType] = unset,
        logs_config: Union[OCILogsConfig, UnsetType] = unset,
        metrics_config: Union[OCIMetricsConfig, UnsetType] = unset,
        regions_config: Union[RegionsConfig, UnsetType] = unset,
        resource_collection_enabled: Union[bool, UnsetType] = unset,
        user_ocid: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``UpdateTenancyConfigDataAttributes`` object.

        :param auth_credentials: The auth credentials of the user. Consists of a public key fingerprint and private key.
        :type auth_credentials: AuthCredentials, optional

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

        :param user_ocid: The OCID of the user needed to authenticate and collect data.
        :type user_ocid: str, optional
        """
        if auth_credentials is not unset:
            kwargs["auth_credentials"] = auth_credentials
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
