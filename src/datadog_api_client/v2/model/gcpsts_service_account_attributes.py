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


class GCPSTSServiceAccountAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_tags": ([str],),
            "automute": (bool,),
            "client_email": (str,),
            "cloud_run_revision_filters": ([str],),
            "host_filters": ([str],),
            "is_cspm_enabled": (bool,),
            "is_security_command_center_enabled": (bool,),
            "resource_collection_enabled": (bool,),
        }

    attribute_map = {
        "account_tags": "account_tags",
        "automute": "automute",
        "client_email": "client_email",
        "cloud_run_revision_filters": "cloud_run_revision_filters",
        "host_filters": "host_filters",
        "is_cspm_enabled": "is_cspm_enabled",
        "is_security_command_center_enabled": "is_security_command_center_enabled",
        "resource_collection_enabled": "resource_collection_enabled",
    }

    def __init__(
        self_,
        account_tags: Union[List[str], UnsetType] = unset,
        automute: Union[bool, UnsetType] = unset,
        client_email: Union[str, UnsetType] = unset,
        cloud_run_revision_filters: Union[List[str], UnsetType] = unset,
        host_filters: Union[List[str], UnsetType] = unset,
        is_cspm_enabled: Union[bool, UnsetType] = unset,
        is_security_command_center_enabled: Union[bool, UnsetType] = unset,
        resource_collection_enabled: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes associated with your service account.

        :param account_tags: Tags to be associated with GCP metrics and service checks from your account.
        :type account_tags: [str], optional

        :param automute: Silence monitors for expected GCE instance shutdowns.
        :type automute: bool, optional

        :param client_email: Your service account email address.
        :type client_email: str, optional

        :param cloud_run_revision_filters: List of filters to limit the Cloud Run revisions that are pulled into Datadog by using tags.
            Only Cloud Run revision resources that apply to specified filters are imported into Datadog.
        :type cloud_run_revision_filters: [str], optional

        :param host_filters: Your Host Filters.
        :type host_filters: [str], optional

        :param is_cspm_enabled: When enabled, Datadog will activate the Cloud Security Monitoring product for this service account. Note: This requires resource_collection_enabled to be set to true.
        :type is_cspm_enabled: bool, optional

        :param is_security_command_center_enabled: When enabled, Datadog will attempt to collect Security Command Center Findings. Note: This requires additional permissions on the service account.
        :type is_security_command_center_enabled: bool, optional

        :param resource_collection_enabled: When enabled, Datadog scans for all resources in your GCP environment.
        :type resource_collection_enabled: bool, optional
        """
        if account_tags is not unset:
            kwargs["account_tags"] = account_tags
        if automute is not unset:
            kwargs["automute"] = automute
        if client_email is not unset:
            kwargs["client_email"] = client_email
        if cloud_run_revision_filters is not unset:
            kwargs["cloud_run_revision_filters"] = cloud_run_revision_filters
        if host_filters is not unset:
            kwargs["host_filters"] = host_filters
        if is_cspm_enabled is not unset:
            kwargs["is_cspm_enabled"] = is_cspm_enabled
        if is_security_command_center_enabled is not unset:
            kwargs["is_security_command_center_enabled"] = is_security_command_center_enabled
        if resource_collection_enabled is not unset:
            kwargs["resource_collection_enabled"] = resource_collection_enabled
        super().__init__(kwargs)
