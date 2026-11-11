# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.feature_flag_suggestion_attributes_current_status import (
        FeatureFlagSuggestionAttributesCurrentStatus,
    )
    from datadog_api_client.v2.model.feature_flag_suggestion_attributes_lifecycle_status import (
        FeatureFlagSuggestionAttributesLifecycleStatus,
    )
    from datadog_api_client.v2.model.feature_flag_suggestion_metadata import FeatureFlagSuggestionMetadata


class FeatureFlagSuggestionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.feature_flag_suggestion_attributes_current_status import (
            FeatureFlagSuggestionAttributesCurrentStatus,
        )
        from datadog_api_client.v2.model.feature_flag_suggestion_attributes_lifecycle_status import (
            FeatureFlagSuggestionAttributesLifecycleStatus,
        )
        from datadog_api_client.v2.model.feature_flag_suggestion_metadata import FeatureFlagSuggestionMetadata

        return {
            "action": (str,),
            "base_flag_history_id": (UUID,),
            "comment": (str,),
            "created_at": (datetime,),
            "created_by": (UUID,),
            "current_status": (FeatureFlagSuggestionAttributesCurrentStatus,),
            "current_value": (str,),
            "deleted_at": (datetime,),
            "deleted_by": (UUID,),
            "environment_id": (UUID,),
            "feature_flag_id": (UUID,),
            "lifecycle_status": (FeatureFlagSuggestionAttributesLifecycleStatus,),
            "message": (str,),
            "_property": (str,),
            "suggestion": (str,),
            "suggestion_metadata": (FeatureFlagSuggestionMetadata,),
            "updated_at": (datetime,),
            "updated_by": (UUID,),
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
        "lifecycle_status": "lifecycle_status",
        "message": "message",
        "_property": "property",
        "suggestion": "suggestion",
        "suggestion_metadata": "suggestion_metadata",
        "updated_at": "updated_at",
        "updated_by": "updated_by",
    }

    def __init__(
        self_,
        action: str,
        base_flag_history_id: UUID,
        created_at: datetime,
        created_by: UUID,
        current_status: FeatureFlagSuggestionAttributesCurrentStatus,
        current_value: str,
        feature_flag_id: UUID,
        lifecycle_status: FeatureFlagSuggestionAttributesLifecycleStatus,
        _property: str,
        suggestion: str,
        comment: Union[str, UnsetType] = unset,
        deleted_at: Union[datetime, UnsetType] = unset,
        deleted_by: Union[UUID, UnsetType] = unset,
        environment_id: Union[UUID, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        suggestion_metadata: Union[FeatureFlagSuggestionMetadata, UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        updated_by: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a feature flag change suggestion.

        :param action: The action proposed by the suggestion.
        :type action: str

        :param base_flag_history_id: The ID of the flag history entry on which the suggestion is based.
        :type base_flag_history_id: UUID

        :param comment: The comment supplied by the suggestion's creator.
        :type comment: str, optional

        :param created_at: The timestamp when the suggestion was created.
        :type created_at: datetime

        :param created_by: The ID of the user who created the suggestion.
        :type created_by: UUID

        :param current_status: The legacy review status. Use ``lifecycle_status`` to distinguish approval from application.
        :type current_status: FeatureFlagSuggestionAttributesCurrentStatus

        :param current_value: The value before the proposed change, serialized as a string.
        :type current_value: str

        :param deleted_at: The timestamp when the suggestion was deleted.
        :type deleted_at: datetime, optional

        :param deleted_by: The ID of the user who deleted the suggestion.
        :type deleted_by: UUID, optional

        :param environment_id: The ID of the environment targeted by the change, if the change is environment-specific.
        :type environment_id: UUID, optional

        :param feature_flag_id: The ID of the feature flag that the suggestion changes.
        :type feature_flag_id: UUID

        :param lifecycle_status: The lifecycle status of the suggestion.
        :type lifecycle_status: FeatureFlagSuggestionAttributesLifecycleStatus

        :param message: A message explaining why a suggestion was created.
        :type message: str, optional

        :param _property: The feature flag property to update.
        :type _property: str

        :param suggestion: The proposed value, serialized as a string. Structured values, such as variants and allocations,
            are JSON-encoded strings.
        :type suggestion: str

        :param suggestion_metadata: Metadata associated with a suggestion. Fields other than ``variant_id`` are set by the server.
        :type suggestion_metadata: FeatureFlagSuggestionMetadata, optional

        :param updated_at: The timestamp when the suggestion was last updated.
        :type updated_at: datetime, optional

        :param updated_by: The ID of the user who last updated the suggestion.
        :type updated_by: UUID, optional
        """
        if comment is not unset:
            kwargs["comment"] = comment
        if deleted_at is not unset:
            kwargs["deleted_at"] = deleted_at
        if deleted_by is not unset:
            kwargs["deleted_by"] = deleted_by
        if environment_id is not unset:
            kwargs["environment_id"] = environment_id
        if message is not unset:
            kwargs["message"] = message
        if suggestion_metadata is not unset:
            kwargs["suggestion_metadata"] = suggestion_metadata
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if updated_by is not unset:
            kwargs["updated_by"] = updated_by
        super().__init__(kwargs)

        self_.action = action
        self_.base_flag_history_id = base_flag_history_id
        self_.created_at = created_at
        self_.created_by = created_by
        self_.current_status = current_status
        self_.current_value = current_value
        self_.feature_flag_id = feature_flag_id
        self_.lifecycle_status = lifecycle_status
        self_._property = _property
        self_.suggestion = suggestion
