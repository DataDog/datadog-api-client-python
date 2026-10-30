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
    from datadog_api_client.v2.model.feature_flag_change_event_suggestion_lifecycle_status import (
        FeatureFlagChangeEventSuggestionLifecycleStatus,
    )
    from datadog_api_client.v2.model.feature_flag_change_event_suggestion_status import (
        FeatureFlagChangeEventSuggestionStatus,
    )


class FeatureFlagChangeEventSuggestionReview(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.feature_flag_change_event_suggestion_lifecycle_status import (
            FeatureFlagChangeEventSuggestionLifecycleStatus,
        )
        from datadog_api_client.v2.model.feature_flag_change_event_suggestion_status import (
            FeatureFlagChangeEventSuggestionStatus,
        )

        return {
            "lifecycle_status": (FeatureFlagChangeEventSuggestionLifecycleStatus,),
            "requester_comment": (str,),
            "reviewer_comment": (str,),
            "status": (FeatureFlagChangeEventSuggestionStatus,),
            "suggestion_created_by": (str,),
        }

    attribute_map = {
        "lifecycle_status": "lifecycle_status",
        "requester_comment": "requester_comment",
        "reviewer_comment": "reviewer_comment",
        "status": "status",
        "suggestion_created_by": "suggestion_created_by",
    }

    def __init__(
        self_,
        lifecycle_status: FeatureFlagChangeEventSuggestionLifecycleStatus,
        status: FeatureFlagChangeEventSuggestionStatus,
        requester_comment: Union[str, UnsetType] = unset,
        reviewer_comment: Union[str, UnsetType] = unset,
        suggestion_created_by: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Review details of a change request that needed approval.
        Present on review events, which ``include_suggestion_events`` adds.
        Also present on a change that an approved change request applied, even when ``include_suggestion_events`` is ``false``.

        :param lifecycle_status: Where the change request is in its lifecycle.
        :type lifecycle_status: FeatureFlagChangeEventSuggestionLifecycleStatus

        :param requester_comment: The comment left by the person who requested the change.
        :type requester_comment: str, optional

        :param reviewer_comment: The comment left by the reviewer.
        :type reviewer_comment: str, optional

        :param status: The review status of the change request.
        :type status: FeatureFlagChangeEventSuggestionStatus

        :param suggestion_created_by: The ID of the user who requested the change.
        :type suggestion_created_by: str, optional
        """
        if requester_comment is not unset:
            kwargs["requester_comment"] = requester_comment
        if reviewer_comment is not unset:
            kwargs["reviewer_comment"] = reviewer_comment
        if suggestion_created_by is not unset:
            kwargs["suggestion_created_by"] = suggestion_created_by
        super().__init__(kwargs)

        self_.lifecycle_status = lifecycle_status
        self_.status = status
