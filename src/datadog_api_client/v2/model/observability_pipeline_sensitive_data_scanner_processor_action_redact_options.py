# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ObservabilityPipelineSensitiveDataScannerProcessorActionRedactOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "replace": (str,),
        }

    attribute_map = {
        "replace": "replace",
    }

    def __init__(self_, replace: str, **kwargs):
        """
        Configuration for fully redacting sensitive data.

        :param replace: The ``ObservabilityPipelineSensitiveDataScannerProcessorActionRedactOptions`` ``replace``.
        :type replace: str
        """
        super().__init__(kwargs)

        self_.replace = replace
