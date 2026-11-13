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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.feature_flag_suggestion_metadata import FeatureFlagSuggestionMetadata


class FeatureFlagApprovalRequiredAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.feature_flag_suggestion_metadata import FeatureFlagSuggestionMetadata

        return {
            "action": (str,),
            "environment_id": (UUID,),
            "_property": (str,),
            "suggestion": (str,),
            "suggestion_metadata": (FeatureFlagSuggestionMetadata,),
        }

    attribute_map = {
        "action": "action",
        "environment_id": "environment_id",
        "_property": "property",
        "suggestion": "suggestion",
        "suggestion_metadata": "suggestion_metadata",
    }

    def __init__(
        self_,
        action: str,
        _property: str,
        suggestion: str,
        environment_id: Union[UUID, UnsetType] = unset,
        suggestion_metadata: Union[FeatureFlagSuggestionMetadata, UnsetType] = unset,
        **kwargs,
    ):
        """
        The change to submit for approval.

        :param action: The proposed action.
        :type action: str

        :param environment_id: The ID of the environment targeted by the change.
        :type environment_id: UUID, optional

        :param _property: The feature flag property to change.
        :type _property: str

        :param suggestion: The proposed value, serialized as a string. Allocation sets are JSON-encoded strings.
        :type suggestion: str

        :param suggestion_metadata: Metadata associated with a suggestion. Fields other than ``variant_id`` are set by the server.
        :type suggestion_metadata: FeatureFlagSuggestionMetadata, optional
        """
        if environment_id is not unset:
            kwargs["environment_id"] = environment_id
        if suggestion_metadata is not unset:
            kwargs["suggestion_metadata"] = suggestion_metadata
        super().__init__(kwargs)

        self_.action = action
        self_._property = _property
        self_.suggestion = suggestion
