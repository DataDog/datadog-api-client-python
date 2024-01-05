# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class AzureAccount(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "app_service_plan_filters": (str,),
            "automute": (bool,),
            "client_id": (str,),
            "client_secret": (str,),
            "container_app_filters": (str,),
            "cspm_enabled": (bool,),
            "custom_metrics_enabled": (bool,),
            "errors": ([str],),
            "host_filters": (str,),
            "new_client_id": (str,),
            "new_tenant_name": (str,),
            "resource_collection_enabled": (bool,),
            "tenant_name": (str,),
        }

    attribute_map = {
        "app_service_plan_filters": "app_service_plan_filters",
        "automute": "automute",
        "client_id": "client_id",
        "client_secret": "client_secret",
        "container_app_filters": "container_app_filters",
        "cspm_enabled": "cspm_enabled",
        "custom_metrics_enabled": "custom_metrics_enabled",
        "errors": "errors",
        "host_filters": "host_filters",
        "new_client_id": "new_client_id",
        "new_tenant_name": "new_tenant_name",
        "resource_collection_enabled": "resource_collection_enabled",
        "tenant_name": "tenant_name",
    }

    def __init__(
        self_,
        app_service_plan_filters: Union[str, UnsetType] = unset,
        automute: Union[bool, UnsetType] = unset,
        client_id: Union[str, UnsetType] = unset,
        client_secret: Union[str, UnsetType] = unset,
        container_app_filters: Union[str, UnsetType] = unset,
        cspm_enabled: Union[bool, UnsetType] = unset,
        custom_metrics_enabled: Union[bool, UnsetType] = unset,
        errors: Union[List[str], UnsetType] = unset,
        host_filters: Union[str, UnsetType] = unset,
        new_client_id: Union[str, UnsetType] = unset,
        new_tenant_name: Union[str, UnsetType] = unset,
        resource_collection_enabled: Union[bool, UnsetType] = unset,
        tenant_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Datadog-Azure integrations configured for your organization.

        :param app_service_plan_filters: Limit the Azure app service plans that are pulled into Datadog using tags.
            Only app service plans that match one of the defined tags are imported into Datadog.
        :type app_service_plan_filters: str, optional

        :param automute: Silence monitors for expected Azure VM shutdowns.
        :type automute: bool, optional

        :param client_id: Your Azure web application ID.
        :type client_id: str, optional

        :param client_secret: Your Azure web application secret key.
        :type client_secret: str, optional

        :param container_app_filters: Limit the Azure container apps that are pulled into Datadog using tags.
            Only container apps that match one of the defined tags are imported into Datadog.
        :type container_app_filters: str, optional

        :param cspm_enabled: When enabled, Datadog’s Cloud Security Management product scans resource configurations monitored by this app registration.
            Note: This requires resource_collection_enabled to be set to true.
        :type cspm_enabled: bool, optional

        :param custom_metrics_enabled: Enable custom metrics for your organization.
        :type custom_metrics_enabled: bool, optional

        :param errors: Errors in your configuration.
        :type errors: [str], optional

        :param host_filters: Limit the Azure instances that are pulled into Datadog by using tags.
            Only hosts that match one of the defined tags are imported into Datadog.
        :type host_filters: str, optional

        :param new_client_id: Your New Azure web application ID.
        :type new_client_id: str, optional

        :param new_tenant_name: Your New Azure Active Directory ID.
        :type new_tenant_name: str, optional

        :param resource_collection_enabled: When enabled, Datadog collects metadata and configuration info from cloud resources (compute instances, databases, load balancers, etc.) monitored by this app registration.
        :type resource_collection_enabled: bool, optional

        :param tenant_name: Your Azure Active Directory ID.
        :type tenant_name: str, optional
        """
        if app_service_plan_filters is not unset:
            kwargs["app_service_plan_filters"] = app_service_plan_filters
        if automute is not unset:
            kwargs["automute"] = automute
        if client_id is not unset:
            kwargs["client_id"] = client_id
        if client_secret is not unset:
            kwargs["client_secret"] = client_secret
        if container_app_filters is not unset:
            kwargs["container_app_filters"] = container_app_filters
        if cspm_enabled is not unset:
            kwargs["cspm_enabled"] = cspm_enabled
        if custom_metrics_enabled is not unset:
            kwargs["custom_metrics_enabled"] = custom_metrics_enabled
        if errors is not unset:
            kwargs["errors"] = errors
        if host_filters is not unset:
            kwargs["host_filters"] = host_filters
        if new_client_id is not unset:
            kwargs["new_client_id"] = new_client_id
        if new_tenant_name is not unset:
            kwargs["new_tenant_name"] = new_tenant_name
        if resource_collection_enabled is not unset:
            kwargs["resource_collection_enabled"] = resource_collection_enabled
        if tenant_name is not unset:
            kwargs["tenant_name"] = tenant_name
        super().__init__(kwargs)
