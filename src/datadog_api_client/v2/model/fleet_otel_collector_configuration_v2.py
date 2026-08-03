# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class FleetOtelCollectorConfigurationV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "collector_id": (str,),
            "compiled_configuration": (str,),
            "distribution": (str,),
        }

    attribute_map = {
        "collector_id": "collector_id",
        "compiled_configuration": "compiled_configuration",
        "distribution": "distribution",
    }

    def __init__(
        self_,
        collector_id: Union[str, UnsetType] = unset,
        compiled_configuration: Union[str, UnsetType] = unset,
        distribution: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration for a single OpenTelemetry collector associated with the agent.

        :param collector_id: The unique identifier of the OpenTelemetry collector.
        :type collector_id: str, optional

        :param compiled_configuration: The final compiled configuration of the OpenTelemetry collector.
        :type compiled_configuration: str, optional

        :param distribution: The distribution of the OpenTelemetry collector.
        :type distribution: str, optional
        """
        if collector_id is not unset:
            kwargs["collector_id"] = collector_id
        if compiled_configuration is not unset:
            kwargs["compiled_configuration"] = compiled_configuration
        if distribution is not unset:
            kwargs["distribution"] = distribution
        super().__init__(kwargs)
