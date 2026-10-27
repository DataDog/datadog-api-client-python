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
    from datadog_api_client.v2.model.tag_indexing_rule_exemption_update_data import TagIndexingRuleExemptionUpdateData


class TagIndexingRuleExemptionUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_indexing_rule_exemption_update_data import (
            TagIndexingRuleExemptionUpdateData,
        )

        return {
            "data": (TagIndexingRuleExemptionUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: TagIndexingRuleExemptionUpdateData, **kwargs):
        """
        Request body for updating a tag indexing rule exemption.

        :param data: Data object for updating a tag indexing rule exemption.
        :type data: TagIndexingRuleExemptionUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
