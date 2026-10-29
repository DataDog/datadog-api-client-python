# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ExecutionPolicySlackScopeRule(ModelNormal):
    validations = {
        "channel_name_selectors": {
            "max_items": 100,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "channel_name_selectors": ([str],),
        }

    attribute_map = {
        "channel_name_selectors": "channel_name_selectors",
    }

    def __init__(self_, channel_name_selectors: List[str], **kwargs):
        """
        A rule restricting a Slack scope to specific private channel names.

        :param channel_name_selectors: The private channel name selectors this rule applies to. Selectors are lowercase private channel names
            without the leading ``#`` , and can contain ``*`` wildcards. Use ``*`` alone to match any private channel name.
        :type channel_name_selectors: [str]
        """
        super().__init__(kwargs)

        self_.channel_name_selectors = channel_name_selectors
