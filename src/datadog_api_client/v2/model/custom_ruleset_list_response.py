# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.custom_ruleset import CustomRuleset


class CustomRulesetListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_ruleset import CustomRuleset

        return {
            "data": ([CustomRuleset],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[CustomRuleset], **kwargs):
        """
        Response containing a list of custom rulesets for the authenticated organization.

        :param data: The list of custom rulesets.
        :type data: [CustomRuleset]
        """
        super().__init__(kwargs)

        self_.data = data
