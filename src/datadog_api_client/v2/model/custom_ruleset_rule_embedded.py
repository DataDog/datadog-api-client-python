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
    from datadog_api_client.v2.model.custom_rule_revision_embedded import CustomRuleRevisionEmbedded


class CustomRulesetRuleEmbedded(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_rule_revision_embedded import CustomRuleRevisionEmbedded

        return {
            "created_at": (datetime,),
            "created_by": (str,),
            "id": (str,),
            "last_revision": (CustomRuleRevisionEmbedded,),
            "name": (str,),
            "revisions": ([CustomRuleRevisionEmbedded], none_type),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "id": "id",
        "last_revision": "last_revision",
        "name": "name",
        "revisions": "revisions",
    }

    def __init__(
        self_,
        created_at: datetime,
        created_by: str,
        id: str,
        last_revision: CustomRuleRevisionEmbedded,
        name: str,
        revisions: Union[List[CustomRuleRevisionEmbedded], none_type],
        **kwargs,
    ):
        """
        A custom static analysis rule as embedded in the rules list of a ruleset response.

        :param created_at: Creation timestamp
        :type created_at: datetime

        :param created_by: Creator identifier
        :type created_by: str

        :param id: Rule identifier, which is the same as the rule name.
        :type id: str

        :param last_revision: A revision of a custom static analysis rule as embedded in a rule or ruleset response.
        :type last_revision: CustomRuleRevisionEmbedded

        :param name: Rule name
        :type name: str

        :param revisions: Revision history of the rule.
        :type revisions: [CustomRuleRevisionEmbedded], none_type
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.id = id
        self_.last_revision = last_revision
        self_.name = name
        self_.revisions = revisions
