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


class OCIMetricsConfig(ModelNormal):
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
        The definition of ``OCIMetricsConfig`` object.

        :param compartment_tag_filters: The compartment tag filters to apply to metric collection. Each value represents a Datadog tag in the format key:value.
        :type compartment_tag_filters: [str], optional

        :param enabled: Enable or disable metric collection. Enabled by default for all services.
        :type enabled: bool, optional

        :param excluded_services: The list of services to exclude from metric collection.
        :type excluded_services: [str], optional
        """
        if compartment_tag_filters is not unset:
            kwargs["compartment_tag_filters"] = compartment_tag_filters
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if excluded_services is not unset:
            kwargs["excluded_services"] = excluded_services
        super().__init__(kwargs)
