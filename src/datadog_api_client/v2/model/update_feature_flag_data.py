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
    from datadog_api_client.v2.model.update_feature_flag_attributes import UpdateFeatureFlagAttributes
    from datadog_api_client.v2.model.update_feature_flag_data_type import UpdateFeatureFlagDataType


class UpdateFeatureFlagData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_feature_flag_attributes import UpdateFeatureFlagAttributes
        from datadog_api_client.v2.model.update_feature_flag_data_type import UpdateFeatureFlagDataType

        return {
            "attributes": (UpdateFeatureFlagAttributes,),
            "type": (UpdateFeatureFlagDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: UpdateFeatureFlagAttributes, type: UpdateFeatureFlagDataType, **kwargs):
        """
        Data for updating a feature flag.

        :param attributes: Attributes for updating a feature flag.
        :type attributes: UpdateFeatureFlagAttributes

        :param type: The resource type.
        :type type: UpdateFeatureFlagDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
