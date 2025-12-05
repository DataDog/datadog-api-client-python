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


class ObservabilityPipelineCustomProcessorRemap(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "drop_on_error": (bool,),
            "enabled": (bool,),
            "include": (str,),
            "name": (str,),
            "source": (str,),
        }

    attribute_map = {
        "drop_on_error": "drop_on_error",
        "enabled": "enabled",
        "include": "include",
        "name": "name",
        "source": "source",
    }

    def __init__(
        self_,
        drop_on_error: bool,
        include: str,
        name: str,
        source: str,
        enabled: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines a single VRL remap rule with its own filtering and transformation logic.

        :param drop_on_error: Whether to drop events that caused errors during processing.
        :type drop_on_error: bool

        :param enabled: Whether this remap rule is enabled.
        :type enabled: bool, optional

        :param include: A Datadog search query used to filter events for this specific remap rule.
        :type include: str

        :param name: A descriptive name for this remap rule.
        :type name: str

        :param source: The VRL script source code that defines the processing logic.
        :type source: str
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        super().__init__(kwargs)

        self_.drop_on_error = drop_on_error
        self_.include = include
        self_.name = name
        self_.source = source
