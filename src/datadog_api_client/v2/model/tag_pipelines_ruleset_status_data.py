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
    from datadog_api_client.v2.model.tag_pipelines_ruleset_status_attributes import TagPipelinesRulesetStatusAttributes
    from datadog_api_client.v2.model.tag_pipelines_ruleset_status_type import TagPipelinesRulesetStatusType


class TagPipelinesRulesetStatusData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tag_pipelines_ruleset_status_attributes import (
            TagPipelinesRulesetStatusAttributes,
        )
        from datadog_api_client.v2.model.tag_pipelines_ruleset_status_type import TagPipelinesRulesetStatusType

        return {
            "attributes": (TagPipelinesRulesetStatusAttributes,),
            "id": (str,),
            "type": (TagPipelinesRulesetStatusType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: TagPipelinesRulesetStatusAttributes, id: str, type: TagPipelinesRulesetStatusType, **kwargs
    ):
        """
        Tag pipeline ruleset status data.

        :param attributes: Attributes for a tag pipeline ruleset status.
        :type attributes: TagPipelinesRulesetStatusAttributes

        :param id: The unique identifier of the ruleset.
        :type id: str

        :param type: Tag pipeline ruleset status resource type.
        :type type: TagPipelinesRulesetStatusType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
