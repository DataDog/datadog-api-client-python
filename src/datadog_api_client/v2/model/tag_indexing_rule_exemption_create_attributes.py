# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TagIndexingRuleExemptionCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "reason": (str,),
        }

    attribute_map = {
        "reason": "reason",
    }

    def __init__(self_, reason: str, **kwargs):
        """
        Attributes for creating a tag indexing rule exemption.

        :param reason: The reason the metric is exempt from tag indexing rules.
        :type reason: str
        """
        super().__init__(kwargs)

        self_.reason = reason
