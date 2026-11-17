# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class MonthlyResourceAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "data_date": (str,),
            "org_name": (str,),
            "public_id": (str,),
            "resource_name": (str,),
            "tags": ({str: (str,)},),
            "timestamp": (str,),
            "usage_type": (str,),
            "usage_value": (float, none_type),
        }

    attribute_map = {
        "data_date": "data_date",
        "org_name": "org_name",
        "public_id": "public_id",
        "resource_name": "resource_name",
        "tags": "tags",
        "timestamp": "timestamp",
        "usage_type": "usage_type",
        "usage_value": "usage_value",
    }

    def __init__(
        self_,
        data_date: Union[str, UnsetType] = unset,
        org_name: Union[str, UnsetType] = unset,
        public_id: Union[str, UnsetType] = unset,
        resource_name: Union[str, UnsetType] = unset,
        tags: Union[Dict[str, str], UnsetType] = unset,
        timestamp: Union[str, UnsetType] = unset,
        usage_type: Union[str, UnsetType] = unset,
        usage_value: Union[float, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Resource usage and organization details for the requested month.

        :param data_date: Date of the source usage data. May be empty when unavailable.
        :type data_date: str, optional

        :param org_name: Name of the organization that owns the resource.
        :type org_name: str, optional

        :param public_id: Public ID of the organization that owns the resource.
        :type public_id: str, optional

        :param resource_name: Name of the resource, such as a host name, metric name, or log index.
        :type resource_name: str, optional

        :param tags: Resource tags when available. Empty for resource types without tag data.
        :type tags: {str: (str,)}, optional

        :param timestamp: Selected billing hour for percentile usage, or the first day of the month for monthly usage. May be empty when unavailable.
        :type timestamp: str, optional

        :param usage_type: Usage type of the resource. Values depend on the billing dimension and are not limited to host types.
        :type usage_type: str, optional

        :param usage_value: Usage attributed to the resource in the units of the requested billing dimension. Values can be fractional.
        :type usage_value: float, none_type, optional
        """
        if data_date is not unset:
            kwargs["data_date"] = data_date
        if org_name is not unset:
            kwargs["org_name"] = org_name
        if public_id is not unset:
            kwargs["public_id"] = public_id
        if resource_name is not unset:
            kwargs["resource_name"] = resource_name
        if tags is not unset:
            kwargs["tags"] = tags
        if timestamp is not unset:
            kwargs["timestamp"] = timestamp
        if usage_type is not unset:
            kwargs["usage_type"] = usage_type
        if usage_value is not unset:
            kwargs["usage_value"] = usage_value
        super().__init__(kwargs)
