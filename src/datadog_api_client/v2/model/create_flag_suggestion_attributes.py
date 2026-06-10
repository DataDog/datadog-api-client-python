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
    from datadog_api_client.v2.model.flag_suggestion_action import FlagSuggestionAction
    from datadog_api_client.v2.model.flag_suggestion_property import FlagSuggestionProperty
    from datadog_api_client.v2.model.suggestion_metadata import SuggestionMetadata


class CreateFlagSuggestionAttributes(ModelNormal):
    validations = {
        "notification_rule_targets": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.flag_suggestion_action import FlagSuggestionAction
        from datadog_api_client.v2.model.flag_suggestion_property import FlagSuggestionProperty
        from datadog_api_client.v2.model.suggestion_metadata import SuggestionMetadata

        return {
            "action": (FlagSuggestionAction,),
            "comment": (str,),
            "environment_id": (UUID,),
            "notification_rule_targets": ([str],),
            "_property": (FlagSuggestionProperty,),
            "suggestion": (str,),
            "suggestion_metadata": (SuggestionMetadata,),
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
        action: FlagSuggestionAction,
        notification_rule_targets: List[str],
        _property: FlagSuggestionProperty,
        comment: Union[str, UnsetType] = unset,
        environment_id: Union[UUID, UnsetType] = unset,
        suggestion: Union[str, UnsetType] = unset,
        suggestion_metadata: Union[SuggestionMetadata, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating a flag suggestion.

        :param action: The type of change action for a suggestion.
        :type action: FlagSuggestionAction

        :param comment: Optional comment explaining the change.
        :type comment: str, optional

        :param environment_id: The environment ID for environment-scoped changes.
        :type environment_id: UUID, optional

        :param notification_rule_targets: Notification handles (without @ prefix) to receive approval or rejection notifications.
            For example, an email address or Slack channel name.
        :type notification_rule_targets: [str]

        :param _property: The flag property being changed.
        :type _property: FlagSuggestionProperty

        :param suggestion: The suggested new value (empty string for flag-level actions like archive, JSON-encoded for complex properties like allocations).
        :type suggestion: str, optional

        :param suggestion_metadata: Optional metadata for a suggestion.
        :type suggestion_metadata: SuggestionMetadata, optional
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
