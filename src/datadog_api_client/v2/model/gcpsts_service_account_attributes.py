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
            "automute": (bool,),
            "client_email": (str,),
            "host_filters": ([str],),
            "is_cspm_enabled": (bool,),
        }

    attribute_map = {
        "automute": "automute",
        "client_email": "client_email",
        "host_filters": "host_filters",
        "is_cspm_enabled": "is_cspm_enabled",
    }

    def __init__(
        self_,
        automute: Union[bool, UnsetType] = unset,
        client_email: Union[str, UnsetType] = unset,
        host_filters: Union[List[str], UnsetType] = unset,
        is_cspm_enabled: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes associated with your service account.

        :param automute: Silence monitors for expected GCE instance shutdowns.
        :type automute: bool, optional

        :param client_email: Your service account email address.
        :type client_email: str, optional

        :param host_filters: Your Host Filters.
        :type host_filters: [str], optional

        :param is_cspm_enabled: When enabled, Datadog performs configuration checks across your Google Cloud environment by continuously scanning every resource.
        :type is_cspm_enabled: bool, optional
        """
        if automute is not unset:
            kwargs["automute"] = automute
        if client_email is not unset:
            kwargs["client_email"] = client_email
        if host_filters is not unset:
            kwargs["host_filters"] = host_filters
        if is_cspm_enabled is not unset:
            kwargs["is_cspm_enabled"] = is_cspm_enabled
        super().__init__(kwargs)
