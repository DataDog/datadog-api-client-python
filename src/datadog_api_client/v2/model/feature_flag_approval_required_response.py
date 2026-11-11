# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.feature_flag_approval_required import FeatureFlagApprovalRequired


class FeatureFlagApprovalRequiredResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.feature_flag_approval_required import FeatureFlagApprovalRequired

        return {
            "data": (FeatureFlagApprovalRequired,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: FeatureFlagApprovalRequired, **kwargs):
        """
        Approval-required response containing a proposed change. No suggestion has been persisted.

        :param data: A proposed change requiring explicit submission through ``CreateFlagSuggestion``.
        :type data: FeatureFlagApprovalRequired
        """
        super().__init__(kwargs)

        self_.data = data
