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


class ObservabilityPipelineSensitiveDataScannerProcessorCustomPatternOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "rule": (str,),
        }

    attribute_map = {
        "description": "description",
        "rule": "rule",
    }

    def __init__(self_, rule: str, description: Union[str, UnsetType] = unset, **kwargs):
        """
        Options for defining a custom regex pattern.

        :param description: Human-readable description providing context about a sensitive data scanner rule
        :type description: str, optional

        :param rule: A regular expression used to detect sensitive values. Must be a valid regex.
        :type rule: str
        """
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.rule = rule
