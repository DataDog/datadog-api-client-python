# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ObservabilityPipelineSensitiveDataScannerProcessorKeywordOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "keywords": ([str],),
            "proximity": (int,),
        }

    attribute_map = {
        "keywords": "keywords",
        "proximity": "proximity",
    }

    def __init__(self_, keywords: List[str], proximity: int, **kwargs):
        """
        Configuration for keywords used to reinforce sensitive data pattern detection.

        :param keywords: A list of keywords to match near the sensitive pattern.
        :type keywords: [str]

        :param proximity: Maximum number of tokens between a keyword and a sensitive value match.
        :type proximity: int
        """
        super().__init__(kwargs)

        self_.keywords = keywords
        self_.proximity = proximity
