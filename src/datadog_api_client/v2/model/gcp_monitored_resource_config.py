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
    from datadog_api_client.v2.model.gcp_monitored_resource_config_type import GCPMonitoredResourceConfigType


class GCPMonitoredResourceConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.gcp_monitored_resource_config_type import GCPMonitoredResourceConfigType

        return {
            "filters": ([str],),
            "type": (GCPMonitoredResourceConfigType,),
        }

    attribute_map = {
        "filters": "filters",
        "type": "type",
    }

    def __init__(
        self_,
        filters: Union[List[str], UnsetType] = unset,
        type: Union[GCPMonitoredResourceConfigType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration for a GCP monitored resource.

        :param filters: List of filters to limit the monitored resources that are pulled into Datadog by using tags.
            Only monitored resources that apply to specified filters are imported into Datadog.
        :type filters: [str], optional

        :param type: The GCP monitored resource type. Only a subset of resource types are supported.
        :type type: GCPMonitoredResourceConfigType, optional
        """
        if filters is not unset:
            kwargs["filters"] = filters
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
