# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rule_based_view_data import RuleBasedViewData


class RuleBasedViewResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rule_based_view_data import RuleBasedViewData

        return {
            "data": (RuleBasedViewData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: RuleBasedViewData, **kwargs):
        """
        Response containing an aggregated view of compliance rules with their finding statistics.

        :param data: Data envelope for the rule-based view response.
        :type data: RuleBasedViewData
        """
        super().__init__(kwargs)

        self_.data = data
