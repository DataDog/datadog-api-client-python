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
    from datadog_api_client.v2.model.update_feature_flag_approvals_attributes import (
        UpdateFeatureFlagApprovalsAttributes,
    )
    from datadog_api_client.v2.model.feature_flag_approvals_data_type import FeatureFlagApprovalsDataType


class UpdateFeatureFlagApprovalsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_feature_flag_approvals_attributes import (
            UpdateFeatureFlagApprovalsAttributes,
        )
        from datadog_api_client.v2.model.feature_flag_approvals_data_type import FeatureFlagApprovalsDataType

        return {
            "attributes": (UpdateFeatureFlagApprovalsAttributes,),
            "type": (FeatureFlagApprovalsDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: UpdateFeatureFlagApprovalsAttributes, type: FeatureFlagApprovalsDataType, **kwargs):
        """
        The feature flag approval setting to update.

        :param attributes: The approval requirement for the flag.
        :type attributes: UpdateFeatureFlagApprovalsAttributes

        :param type: The resource type for feature flag approval settings.
        :type type: FeatureFlagApprovalsDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
