# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.flag_suggestion_action import FlagSuggestionAction
    from datadog_api_client.v2.model.flag_suggestion_status import FlagSuggestionStatus
    from datadog_api_client.v2.model.flag_suggestion_property import FlagSuggestionProperty
    from datadog_api_client.v2.model.suggestion_metadata import SuggestionMetadata


class FlagSuggestionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.flag_suggestion_action import FlagSuggestionAction
        from datadog_api_client.v2.model.flag_suggestion_status import FlagSuggestionStatus
        from datadog_api_client.v2.model.flag_suggestion_property import FlagSuggestionProperty
        from datadog_api_client.v2.model.suggestion_metadata import SuggestionMetadata

        return {
            "action": (FlagSuggestionAction,),
            "base_flag_history_id": (UUID,),
            "comment": (str, none_type),
            "created_at": (datetime,),
            "created_by": (UUID,),
            "current_status": (FlagSuggestionStatus,),
            "current_value": (str,),
            "deleted_at": (datetime, none_type),
            "deleted_by": (str, none_type),
            "environment_id": (str, none_type),
            "feature_flag_id": (UUID,),
            "message": (str,),
            "_property": (FlagSuggestionProperty,),
            "suggestion": (str,),
            "suggestion_metadata": (SuggestionMetadata,),
            "updated_at": (datetime, none_type),
            "updated_by": (str, none_type),
        }

    attribute_map = {
        "action": "action",
        "base_flag_history_id": "base_flag_history_id",
        "comment": "comment",
        "created_at": "created_at",
        "created_by": "created_by",
        "current_status": "current_status",
        "current_value": "current_value",
        "deleted_at": "deleted_at",
        "deleted_by": "deleted_by",
        "environment_id": "environment_id",
        "feature_flag_id": "feature_flag_id",
        "message": "message",
        "_property": "property",
        "suggestion": "suggestion",
        "suggestion_metadata": "suggestion_metadata",
        "updated_at": "updated_at",
        "updated_by": "updated_by",
    }

    def __init__(
        self_,
        action: FlagSuggestionAction,
        created_at: datetime,
        created_by: UUID,
        current_status: FlagSuggestionStatus,
        feature_flag_id: UUID,
        _property: FlagSuggestionProperty,
        base_flag_history_id: Union[UUID, UnsetType] = unset,
        comment: Union[str, none_type, UnsetType] = unset,
        current_value: Union[str, UnsetType] = unset,
        deleted_at: Union[datetime, none_type, UnsetType] = unset,
        deleted_by: Union[str, none_type, UnsetType] = unset,
        environment_id: Union[str, none_type, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        suggestion: Union[str, UnsetType] = unset,
        suggestion_metadata: Union[SuggestionMetadata, UnsetType] = unset,
        updated_at: Union[datetime, none_type, UnsetType] = unset,
        updated_by: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a flag suggestion.

        :param action: The type of change action for a suggestion.
        :type action: FlagSuggestionAction

        :param base_flag_history_id: The flag history version this suggestion was based on.
        :type base_flag_history_id: UUID, optional

        :param comment: Optional comment from the requester.
        :type comment: str, none_type, optional

        :param created_at: When the suggestion was created.
        :type created_at: datetime

        :param created_by: UUID of the user who created the suggestion.
        :type created_by: UUID

        :param current_status: The status of a flag suggestion.
        :type current_status: FlagSuggestionStatus

        :param current_value: The current value before the suggested change (empty string for flag-level actions like archive).
        :type current_value: str, optional

        :param deleted_at: When the suggestion was soft-deleted.
        :type deleted_at: datetime, none_type, optional

        :param deleted_by: UUID of the user who deleted the suggestion.
        :type deleted_by: str, none_type, optional

        :param environment_id: The environment ID for environment-scoped suggestions. Null for flag-level changes.
        :type environment_id: str, none_type, optional

        :param feature_flag_id: The ID of the feature flag this suggestion applies to.
        :type feature_flag_id: UUID

        :param message: Human-readable message about the suggestion (populated on auto-created suggestions).
        :type message: str, optional

        :param _property: The flag property being changed.
        :type _property: FlagSuggestionProperty

        :param suggestion: The suggested new value (JSON-encoded for complex properties, empty string for flag-level actions like archive).
        :type suggestion: str, optional

        :param suggestion_metadata: Optional metadata for a suggestion.
        :type suggestion_metadata: SuggestionMetadata, optional

        :param updated_at: When the suggestion was last updated.
        :type updated_at: datetime, none_type, optional

        :param updated_by: UUID of the user who last updated the suggestion.
        :type updated_by: str, none_type, optional
        """
        if base_flag_history_id is not unset:
            kwargs["base_flag_history_id"] = base_flag_history_id
        if comment is not unset:
            kwargs["comment"] = comment
        if current_value is not unset:
            kwargs["current_value"] = current_value
        if deleted_at is not unset:
            kwargs["deleted_at"] = deleted_at
        if deleted_by is not unset:
            kwargs["deleted_by"] = deleted_by
        if environment_id is not unset:
            kwargs["environment_id"] = environment_id
        if message is not unset:
            kwargs["message"] = message
        if suggestion is not unset:
            kwargs["suggestion"] = suggestion
        if suggestion_metadata is not unset:
            kwargs["suggestion_metadata"] = suggestion_metadata
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if updated_by is not unset:
            kwargs["updated_by"] = updated_by
        super().__init__(kwargs)

        self_.action = action
        self_.created_at = created_at
        self_.created_by = created_by
        self_.current_status = current_status
        self_.feature_flag_id = feature_flag_id
        self_._property = _property
