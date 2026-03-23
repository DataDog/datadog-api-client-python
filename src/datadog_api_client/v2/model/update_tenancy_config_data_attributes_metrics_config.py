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


class UpdateTenancyConfigDataAttributesMetricsConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "compartment_tag_filters": ([str],),
            "enabled": (bool,),
            "excluded_services": ([str],),
        }

    attribute_map = {
        "compartment_tag_filters": "compartment_tag_filters",
        "enabled": "enabled",
        "excluded_services": "excluded_services",
    }

    def __init__(
        self_,
        compartment_tag_filters: Union[List[str], UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        excluded_services: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Metrics collection configuration for updating an OCI tenancy, controlling which compartments and services are included or excluded.

        :param compartment_tag_filters: List of compartment tag filters to scope metrics collection to specific compartments.
        :type compartment_tag_filters: [str], optional

        :param enabled: Whether metrics collection is enabled for the tenancy.
        :type enabled: bool, optional

        :param excluded_services: List of OCI service names to exclude from metrics collection.
        :type excluded_services: [str], optional
        """
        if compartment_tag_filters is not unset:
            kwargs["compartment_tag_filters"] = compartment_tag_filters
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if excluded_services is not unset:
            kwargs["excluded_services"] = excluded_services
        super().__init__(kwargs)
