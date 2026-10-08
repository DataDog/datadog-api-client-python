# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RecommendationV2RequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "arguments": ([str],),
        }

    attribute_map = {
        "arguments": "arguments",
    }

    def __init__(self_, arguments: List[str], **kwargs):
        """
        Attributes for requesting SPA recommendations by forwarding a Spark job's raw arguments
        instead of a pre-computed shard.

        :param arguments: Raw, unfiltered Spark job arguments as submitted (for example, ``--org_id=2`` ).
            SPA determines which arguments are relevant for the given service.
        :type arguments: [str]
        """
        super().__init__(kwargs)

        self_.arguments = arguments
