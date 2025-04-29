# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ObservabilityPipelineSensitiveDataScannerProcessorCustomPatternOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "rule": (str,),
        }

    attribute_map = {
        "rule": "rule",
    }

    def __init__(self_, rule: str, **kwargs):
        """
        Options for defining a custom regex pattern.

        :param rule: A regular expression used to detect sensitive values. Must be a valid regex.
        :type rule: str
        """
        super().__init__(kwargs)

        self_.rule = rule
