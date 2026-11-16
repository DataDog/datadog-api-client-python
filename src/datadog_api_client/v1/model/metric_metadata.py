# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class MetricMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str, none_type),
            "integration": (str, none_type),
            "per_unit": (str, none_type),
            "short_name": (str, none_type),
            "statsd_interval": (int, none_type),
            "type": (str, none_type),
            "unit": (str, none_type),
        }

    attribute_map = {
        "description": "description",
        "integration": "integration",
        "per_unit": "per_unit",
        "short_name": "short_name",
        "statsd_interval": "statsd_interval",
        "type": "type",
        "unit": "unit",
    }
    read_only_vars = {
        "integration",
    }

    def __init__(
        self_,
        description: Union[str, none_type, UnsetType] = unset,
        integration: Union[str, none_type, UnsetType] = unset,
        per_unit: Union[str, none_type, UnsetType] = unset,
        short_name: Union[str, none_type, UnsetType] = unset,
        statsd_interval: Union[int, none_type, UnsetType] = unset,
        type: Union[str, none_type, UnsetType] = unset,
        unit: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object with all metric related metadata.

        :param description: Metric description.
        :type description: str, none_type, optional

        :param integration: Name of the integration that sent the metric if applicable.
        :type integration: str, none_type, optional

        :param per_unit: Per unit of the metric such as ``second`` in ``bytes per second``.
        :type per_unit: str, none_type, optional

        :param short_name: A more human-readable and abbreviated version of the metric name.
        :type short_name: str, none_type, optional

        :param statsd_interval: StatsD flush interval of the metric in seconds if applicable.
        :type statsd_interval: int, none_type, optional

        :param type: Metric type such as ``gauge`` or ``rate``.
        :type type: str, none_type, optional

        :param unit: Primary unit of the metric such as ``byte`` or ``operation``.
        :type unit: str, none_type, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if integration is not unset:
            kwargs["integration"] = integration
        if per_unit is not unset:
            kwargs["per_unit"] = per_unit
        if short_name is not unset:
            kwargs["short_name"] = short_name
        if statsd_interval is not unset:
            kwargs["statsd_interval"] = statsd_interval
        if type is not unset:
            kwargs["type"] = type
        if unit is not unset:
            kwargs["unit"] = unit
        super().__init__(kwargs)
