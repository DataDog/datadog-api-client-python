# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.org_group_policy_suggestion_attributes import OrgGroupPolicySuggestionAttributes
    from datadog_api_client.v2.model.org_group_policy_suggestion_relationships import (
        OrgGroupPolicySuggestionRelationships,
    )
    from datadog_api_client.v2.model.org_group_policy_suggestion_type import OrgGroupPolicySuggestionType


class OrgGroupPolicySuggestionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_policy_suggestion_attributes import (
            OrgGroupPolicySuggestionAttributes,
        )
        from datadog_api_client.v2.model.org_group_policy_suggestion_relationships import (
            OrgGroupPolicySuggestionRelationships,
        )
        from datadog_api_client.v2.model.org_group_policy_suggestion_type import OrgGroupPolicySuggestionType

        return {
            "attributes": (OrgGroupPolicySuggestionAttributes,),
            "id": (str,),
            "relationships": (OrgGroupPolicySuggestionRelationships,),
            "type": (OrgGroupPolicySuggestionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: OrgGroupPolicySuggestionAttributes,
        id: str,
        type: OrgGroupPolicySuggestionType,
        relationships: Union[OrgGroupPolicySuggestionRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        An org group policy suggestion resource.

        :param attributes: Attributes of an org group policy suggestion.
        :type attributes: OrgGroupPolicySuggestionAttributes

        :param id: The ID of the org group policy suggestion.
        :type id: str

        :param relationships: Relationships of an org group policy suggestion.
        :type relationships: OrgGroupPolicySuggestionRelationships, optional

        :param type: Org group policy suggestions resource type.
        :type type: OrgGroupPolicySuggestionType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
