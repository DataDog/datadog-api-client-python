# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.feature_flag_approval_required_attributes import (
        FeatureFlagApprovalRequiredAttributes,
    )
    from datadog_api_client.v2.model.feature_flag_approval_required_data_type import FeatureFlagApprovalRequiredDataType


class FeatureFlagApprovalRequired(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.feature_flag_approval_required_attributes import (
            FeatureFlagApprovalRequiredAttributes,
        )
        from datadog_api_client.v2.model.feature_flag_approval_required_data_type import (
            FeatureFlagApprovalRequiredDataType,
        )

        return {
            "attributes": (FeatureFlagApprovalRequiredAttributes,),
            "id": (UUID,),
            "type": (FeatureFlagApprovalRequiredDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: FeatureFlagApprovalRequiredAttributes,
        id: UUID,
        type: FeatureFlagApprovalRequiredDataType,
        **kwargs,
    ):
        """
        A proposed change requiring explicit submission through ``CreateFlagSuggestion``.

        :param attributes: The change to submit for approval.
        :type attributes: FeatureFlagApprovalRequiredAttributes

        :param id: The ID of the feature flag. This is not a suggestion ID.
        :type id: UUID

        :param type: The resource type for an approval-required response.
        :type type: FeatureFlagApprovalRequiredDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
