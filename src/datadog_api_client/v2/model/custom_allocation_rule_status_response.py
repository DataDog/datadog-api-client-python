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
    from datadog_api_client.v2.model.custom_allocation_rule_status_data import CustomAllocationRuleStatusData


class CustomAllocationRuleStatusResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_allocation_rule_status_data import CustomAllocationRuleStatusData

        return {
            "data": ([CustomAllocationRuleStatusData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[CustomAllocationRuleStatusData], **kwargs):
        """
        List of custom allocation rule statuses.

        :param data: List of custom allocation rule statuses.
        :type data: [CustomAllocationRuleStatusData]
        """
        super().__init__(kwargs)

        self_.data = data
