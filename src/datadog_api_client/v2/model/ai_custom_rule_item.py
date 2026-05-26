# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_custom_rule_revision_response_attributes import (
        AiCustomRuleRevisionResponseAttributes,
    )


class AiCustomRuleItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_custom_rule_revision_response_attributes import (
            AiCustomRuleRevisionResponseAttributes,
        )

        return {
            "created_at": (datetime,),
            "created_by": (str,),
            "last_revision": (AiCustomRuleRevisionResponseAttributes,),
            "name": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "last_revision": "last_revision",
        "name": "name",
    }

    def __init__(
        self_,
        created_at: datetime,
        created_by: str,
        last_revision: AiCustomRuleRevisionResponseAttributes,
        name: str,
        **kwargs,
    ):
        """
        An AI custom rule embedded within a ruleset response.

        :param created_at: The creation timestamp.
        :type created_at: datetime

        :param created_by: The identifier of the user who created the rule.
        :type created_by: str

        :param last_revision: Response attributes of an AI custom rule revision.
        :type last_revision: AiCustomRuleRevisionResponseAttributes

        :param name: The rule name.
        :type name: str
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.last_revision = last_revision
        self_.name = name
