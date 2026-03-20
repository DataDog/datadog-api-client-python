# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "fields": ([str],),
        }

    attribute_map = {
        "fields": "fields",
    }

    def __init__(self_, fields: List[str], **kwargs):
        """
        Fields to which the scope rule applies.

        :param fields: The ``ObservabilityPipelineSensitiveDataScannerProcessorScopeOptions`` ``fields``.
        :type fields: [str]
        """
        super().__init__(kwargs)

        self_.fields = fields
