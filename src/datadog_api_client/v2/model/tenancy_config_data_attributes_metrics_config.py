# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class TenancyConfigDataAttributesMetricsConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "compartment_tag_filters": ([str],),
            "enabled": (bool,),
            "excluded_services": ([str],),
            "resource_tag_filters": ({str: ([str],)},),
        }

    attribute_map = {
        "compartment_tag_filters": "compartment_tag_filters",
        "enabled": "enabled",
        "excluded_services": "excluded_services",
        "resource_tag_filters": "resource_tag_filters",
    }

    def __init__(
        self_,
        compartment_tag_filters: Union[List[str], UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        excluded_services: Union[List[str], UnsetType] = unset,
        resource_tag_filters: Union[Dict[str, List[str]], UnsetType] = unset,
        **kwargs,
    ):
        """
        Metrics collection configuration for an OCI tenancy, indicating which compartments and services are included or excluded.

        :param compartment_tag_filters: List of compartment tag filters scoping metrics collection to specific compartments.
        :type compartment_tag_filters: [str], optional

        :param enabled: Whether metrics collection is enabled for the tenancy.
        :type enabled: bool, optional

        :param excluded_services: List of OCI service names excluded from metrics collection.
        :type excluded_services: [str], optional

        :param resource_tag_filters: Map of OCI service names to the resource tag filters that scope metrics collection for that service.
        :type resource_tag_filters: {str: ([str],)}, optional
        """
        if compartment_tag_filters is not unset:
            kwargs["compartment_tag_filters"] = compartment_tag_filters
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if excluded_services is not unset:
            kwargs["excluded_services"] = excluded_services
        if resource_tag_filters is not unset:
            kwargs["resource_tag_filters"] = resource_tag_filters
        super().__init__(kwargs)
