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
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.feature_flag_change_event_action import FeatureFlagChangeEventAction
    from datadog_api_client.v2.model.feature_flag_change_event_creation_source import (
        FeatureFlagChangeEventCreationSource,
    )
    from datadog_api_client.v2.model.feature_flag_change_event_environment import FeatureFlagChangeEventEnvironment
    from datadog_api_client.v2.model.feature_flag_change_event_flag import FeatureFlagChangeEventFlag
    from datadog_api_client.v2.model.feature_flag_change_event_property import FeatureFlagChangeEventProperty
    from datadog_api_client.v2.model.feature_flag_change_event_suggestion_review import (
        FeatureFlagChangeEventSuggestionReview,
    )


class FeatureFlagChangeEventAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.feature_flag_change_event_action import FeatureFlagChangeEventAction
        from datadog_api_client.v2.model.feature_flag_change_event_creation_source import (
            FeatureFlagChangeEventCreationSource,
        )
        from datadog_api_client.v2.model.feature_flag_change_event_environment import FeatureFlagChangeEventEnvironment
        from datadog_api_client.v2.model.feature_flag_change_event_flag import FeatureFlagChangeEventFlag
        from datadog_api_client.v2.model.feature_flag_change_event_property import FeatureFlagChangeEventProperty
        from datadog_api_client.v2.model.feature_flag_change_event_suggestion_review import (
            FeatureFlagChangeEventSuggestionReview,
        )

        return {
            "action": (FeatureFlagChangeEventAction,),
            "change_metadata": (str, none_type),
            "creation_source": (FeatureFlagChangeEventCreationSource,),
            "description": (str,),
            "environment": (FeatureFlagChangeEventEnvironment,),
            "feature_flag": (FeatureFlagChangeEventFlag,),
            "new_value": (str, none_type),
            "previous_value": (str, none_type),
            "_property": (FeatureFlagChangeEventProperty,),
            "suggestion_review": (FeatureFlagChangeEventSuggestionReview,),
            "timestamp": (datetime,),
            "user_id": (str, none_type),
            "version_number": (int,),
        }

    attribute_map = {
        "action": "action",
        "change_metadata": "change_metadata",
        "creation_source": "creation_source",
        "description": "description",
        "environment": "environment",
        "feature_flag": "feature_flag",
        "new_value": "new_value",
        "previous_value": "previous_value",
        "_property": "property",
        "suggestion_review": "suggestion_review",
        "timestamp": "timestamp",
        "user_id": "user_id",
        "version_number": "version_number",
    }

    def __init__(
        self_,
        action: FeatureFlagChangeEventAction,
        feature_flag: FeatureFlagChangeEventFlag,
        _property: FeatureFlagChangeEventProperty,
        timestamp: datetime,
        version_number: int,
        change_metadata: Union[str, none_type, UnsetType] = unset,
        creation_source: Union[FeatureFlagChangeEventCreationSource, none_type, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        environment: Union[FeatureFlagChangeEventEnvironment, none_type, UnsetType] = unset,
        new_value: Union[str, none_type, UnsetType] = unset,
        previous_value: Union[str, none_type, UnsetType] = unset,
        suggestion_review: Union[FeatureFlagChangeEventSuggestionReview, UnsetType] = unset,
        user_id: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a feature flag change event.

        :param action: The kind of change.
        :type action: FeatureFlagChangeEventAction

        :param change_metadata: Additional details about the change, as a JSON-encoded string.
        :type change_metadata: str, none_type, optional

        :param creation_source: Where the change was made: ``UI`` for the Datadog app, or ``MCP`` for a Model Context Protocol (MCP) client.
        :type creation_source: FeatureFlagChangeEventCreationSource, none_type, optional

        :param description: A readable sentence describing the change, as shown on the flag history page and in the Action column of the CSV export.
        :type description: str, optional

        :param environment: The environment the change applies to. Null for a change to the flag itself rather than to one environment.
        :type environment: FeatureFlagChangeEventEnvironment, none_type, optional

        :param feature_flag: The feature flag the change applies to.
        :type feature_flag: FeatureFlagChangeEventFlag

        :param new_value: The value after the change, serialized as a string.
        :type new_value: str, none_type, optional

        :param previous_value: The value before the change, serialized as a string.
        :type previous_value: str, none_type, optional

        :param _property: The part of the feature flag the change applies to.
        :type _property: FeatureFlagChangeEventProperty

        :param suggestion_review: Review details of a change request that needed approval.
            Present on review events, which ``include_suggestion_events`` adds.
            Also present on a change that an approved change request applied, even when ``include_suggestion_events`` is ``false``.
        :type suggestion_review: FeatureFlagChangeEventSuggestionReview, optional

        :param timestamp: When the change was made.
        :type timestamp: datetime

        :param user_id: The ID of the user who made the change. Null when no user made the change.
        :type user_id: str, none_type, optional

        :param version_number: The version of the feature flag the change produced.
        :type version_number: int
        """
        if change_metadata is not unset:
            kwargs["change_metadata"] = change_metadata
        if creation_source is not unset:
            kwargs["creation_source"] = creation_source
        if description is not unset:
            kwargs["description"] = description
        if environment is not unset:
            kwargs["environment"] = environment
        if new_value is not unset:
            kwargs["new_value"] = new_value
        if previous_value is not unset:
            kwargs["previous_value"] = previous_value
        if suggestion_review is not unset:
            kwargs["suggestion_review"] = suggestion_review
        if user_id is not unset:
            kwargs["user_id"] = user_id
        super().__init__(kwargs)

        self_.action = action
        self_.feature_flag = feature_flag
        self_._property = _property
        self_.timestamp = timestamp
        self_.version_number = version_number
