# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.feature_flag_suggestion_metadata_request import (
        FeatureFlagSuggestionMetadataRequest,
    )


class CreateFlagSuggestionAttributes(ModelNormal):
    validations = {
        "notification_rule_targets": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.feature_flag_suggestion_metadata_request import (
            FeatureFlagSuggestionMetadataRequest,
        )

        return {
            "action": (str,),
            "comment": (str,),
            "environment_id": (UUID,),
            "notification_rule_targets": ([str],),
            "_property": (str,),
            "suggestion": (str,),
            "suggestion_metadata": (FeatureFlagSuggestionMetadataRequest,),
        }

    attribute_map = {
        "action": "action",
        "comment": "comment",
        "environment_id": "environment_id",
        "notification_rule_targets": "notification_rule_targets",
        "_property": "property",
        "suggestion": "suggestion",
        "suggestion_metadata": "suggestion_metadata",
    }

    def __init__(
        self_,
        action: str,
        notification_rule_targets: List[str],
        _property: str,
        comment: Union[str, UnsetType] = unset,
        environment_id: Union[UUID, UnsetType] = unset,
        suggestion: Union[str, UnsetType] = unset,
        suggestion_metadata: Union[FeatureFlagSuggestionMetadataRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating a feature flag change suggestion.

        :param action: The action proposed by the suggestion.
        :type action: str

        :param comment: A comment explaining the proposed change.
        :type comment: str, optional

        :param environment_id: The ID of the target environment. Required for ``ALLOCATIONS`` , ``DEFAULT_VARIANT`` , and
            ``OVERRIDE_VARIANT`` changes.
        :type environment_id: UUID, optional

        :param notification_rule_targets: Handles to notify about the review, without the ``@`` prefix. For example, an email address
            or a Slack channel name.
        :type notification_rule_targets: [str]

        :param _property: The property to change. The property must require approval for this flag and environment.
        :type _property: str

        :param suggestion: The proposed value as a string. For structured values, supply a JSON-encoded string.
        :type suggestion: str, optional

        :param suggestion_metadata: Client-settable metadata for a suggestion.
        :type suggestion_metadata: FeatureFlagSuggestionMetadataRequest, optional
        """
        if comment is not unset:
            kwargs["comment"] = comment
        if environment_id is not unset:
            kwargs["environment_id"] = environment_id
        if suggestion is not unset:
            kwargs["suggestion"] = suggestion
        if suggestion_metadata is not unset:
            kwargs["suggestion_metadata"] = suggestion_metadata
        super().__init__(kwargs)

        self_.action = action
        self_.notification_rule_targets = notification_rule_targets
        self_._property = _property
