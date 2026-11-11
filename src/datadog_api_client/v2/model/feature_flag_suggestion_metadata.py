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
    from datadog_api_client.v2.model.feature_flag_suggestion_experiment_action import (
        FeatureFlagSuggestionExperimentAction,
    )


class FeatureFlagSuggestionMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.feature_flag_suggestion_experiment_action import (
            FeatureFlagSuggestionExperimentAction,
        )

        return {
            "allow_draft_reorder": (bool,),
            "experiment_action": (FeatureFlagSuggestionExperimentAction,),
            "experiment_action_request_fingerprint": (str,),
            "variant_id": (UUID,),
        }

    attribute_map = {
        "allow_draft_reorder": "allow_draft_reorder",
        "experiment_action": "experiment_action",
        "experiment_action_request_fingerprint": "experiment_action_request_fingerprint",
        "variant_id": "variant_id",
    }

    def __init__(
        self_,
        allow_draft_reorder: Union[bool, UnsetType] = unset,
        experiment_action: Union[FeatureFlagSuggestionExperimentAction, UnsetType] = unset,
        experiment_action_request_fingerprint: Union[str, UnsetType] = unset,
        variant_id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata associated with a suggestion. Fields other than ``variant_id`` are set by the server.

        :param allow_draft_reorder: Whether the server allows this allocation suggestion to reorder persisted drafts.
        :type allow_draft_reorder: bool, optional

        :param experiment_action: Server-generated reference to an experiment action requiring approval.
        :type experiment_action: FeatureFlagSuggestionExperimentAction, optional

        :param experiment_action_request_fingerprint: Server-generated fingerprint of the experiment action request.
        :type experiment_action_request_fingerprint: str, optional

        :param variant_id: The ID of the variant targeted by the suggestion.
        :type variant_id: UUID, optional
        """
        if allow_draft_reorder is not unset:
            kwargs["allow_draft_reorder"] = allow_draft_reorder
        if experiment_action is not unset:
            kwargs["experiment_action"] = experiment_action
        if experiment_action_request_fingerprint is not unset:
            kwargs["experiment_action_request_fingerprint"] = experiment_action_request_fingerprint
        if variant_id is not unset:
            kwargs["variant_id"] = variant_id
        super().__init__(kwargs)
