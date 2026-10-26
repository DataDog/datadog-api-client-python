# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.custom_rule_nullable_revision_embedded import CustomRuleNullableRevisionEmbedded
    from datadog_api_client.v2.model.custom_rule_revision_embedded import CustomRuleRevisionEmbedded


class CustomRuleAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_rule_nullable_revision_embedded import (
            CustomRuleNullableRevisionEmbedded,
        )
        from datadog_api_client.v2.model.custom_rule_revision_embedded import CustomRuleRevisionEmbedded

        return {
            "created_at": (datetime,),
            "created_by": (str,),
            "last_revision": (CustomRuleNullableRevisionEmbedded,),
            "name": (str,),
            "revisions": ([CustomRuleRevisionEmbedded], none_type),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "last_revision": "last_revision",
        "name": "name",
        "revisions": "revisions",
    }

    def __init__(
        self_,
        created_at: datetime,
        created_by: str,
        last_revision: Union[CustomRuleNullableRevisionEmbedded, none_type],
        name: str,
        revisions: Union[List[CustomRuleRevisionEmbedded], none_type],
        **kwargs,
    ):
        """
        Attributes of a custom static analysis rule, including its most recent revision and revision history.

        :param created_at: Creation timestamp
        :type created_at: datetime

        :param created_by: Creator identifier
        :type created_by: str

        :param last_revision: The most recent revision of the rule, or null when the rule has no revisions.
        :type last_revision: CustomRuleNullableRevisionEmbedded, none_type

        :param name: Rule name
        :type name: str

        :param revisions: Revision history of the rule.
        :type revisions: [CustomRuleRevisionEmbedded], none_type
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.last_revision = last_revision
        self_.name = name
        self_.revisions = revisions
