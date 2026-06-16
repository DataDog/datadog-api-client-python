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
    from datadog_api_client.v2.model.tag_indexing_rule_exemption_create_attributes import (
        TagIndexingRuleExemptionCreateAttributes,
    )
    from datadog_api_client.v2.model.tag_indexing_rule_exemption_type import TagIndexingRuleExemptionType


class TagIndexingRuleExemptionCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_indexing_rule_exemption_create_attributes import (
            TagIndexingRuleExemptionCreateAttributes,
        )
        from datadog_api_client.v2.model.tag_indexing_rule_exemption_type import TagIndexingRuleExemptionType

        return {
            "attributes": (TagIndexingRuleExemptionCreateAttributes,),
            "type": (TagIndexingRuleExemptionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: TagIndexingRuleExemptionCreateAttributes, type: TagIndexingRuleExemptionType, **kwargs
    ):
        """
        Data object for creating a tag indexing rule exemption.

        :param attributes: Attributes for creating a tag indexing rule exemption.
        :type attributes: TagIndexingRuleExemptionCreateAttributes

        :param type: The tag indexing rule exemption resource type.
        :type type: TagIndexingRuleExemptionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
