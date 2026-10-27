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
    from datadog_api_client.v2.model.tag_indexing_rule_exemption_update_attributes import (
        TagIndexingRuleExemptionUpdateAttributes,
    )
    from datadog_api_client.v2.model.tag_indexing_rule_exemption_type import TagIndexingRuleExemptionType


class TagIndexingRuleExemptionUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_indexing_rule_exemption_update_attributes import (
            TagIndexingRuleExemptionUpdateAttributes,
        )
        from datadog_api_client.v2.model.tag_indexing_rule_exemption_type import TagIndexingRuleExemptionType

        return {
            "attributes": (TagIndexingRuleExemptionUpdateAttributes,),
            "type": (TagIndexingRuleExemptionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: TagIndexingRuleExemptionUpdateAttributes, type: TagIndexingRuleExemptionType, **kwargs
    ):
        """
        Data object for updating a tag indexing rule exemption.

        :param attributes: Attributes for updating a tag indexing rule exemption.
        :type attributes: TagIndexingRuleExemptionUpdateAttributes

        :param type: The tag indexing rule exemption resource type.
        :type type: TagIndexingRuleExemptionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
