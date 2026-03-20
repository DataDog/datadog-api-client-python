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
    from datadog_api_client.v2.model.create_feature_flag_attributes import CreateFeatureFlagAttributes
    from datadog_api_client.v2.model.create_feature_flag_data_type import CreateFeatureFlagDataType


class CreateFeatureFlagData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_feature_flag_attributes import CreateFeatureFlagAttributes
        from datadog_api_client.v2.model.create_feature_flag_data_type import CreateFeatureFlagDataType

        return {
            "attributes": (CreateFeatureFlagAttributes,),
            "type": (CreateFeatureFlagDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: CreateFeatureFlagAttributes, type: CreateFeatureFlagDataType, **kwargs):
        """
        Data for creating a new feature flag.

        :param attributes: Attributes for creating a new feature flag.
        :type attributes: CreateFeatureFlagAttributes

        :param type: The resource type.
        :type type: CreateFeatureFlagDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
