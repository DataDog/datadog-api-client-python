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
    from datadog_api_client.v2.model.default_inbox_rule_data_response import DefaultInboxRuleDataResponse


class DefaultInboxRulesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.default_inbox_rule_data_response import DefaultInboxRuleDataResponse

        return {
            "data": ([DefaultInboxRuleDataResponse],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[DefaultInboxRuleDataResponse], **kwargs):
        """
        A list of default inbox rules.

        :param data: A list of default inbox rule data objects.
        :type data: [DefaultInboxRuleDataResponse]
        """
        super().__init__(kwargs)

        self_.data = data
