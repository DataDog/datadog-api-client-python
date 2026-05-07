# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CostTagPipelineActiveKeyAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "rule_count": (int,),
        }

    attribute_map = {
        "rule_count": "rule_count",
    }

    def __init__(self_, rule_count: int, **kwargs):
        """
        Attributes for an active tag pipeline key.

        :param rule_count: The number of tag pipeline rules that set this tag key.
        :type rule_count: int
        """
        super().__init__(kwargs)

        self_.rule_count = rule_count
