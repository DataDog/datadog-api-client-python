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
    from datadog_api_client.v2.model.feature_flag_attributes import FeatureFlagAttributes
    from datadog_api_client.v2.model.create_feature_flag_data_type import CreateFeatureFlagDataType


class FeatureFlag(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.feature_flag_attributes import FeatureFlagAttributes
        from datadog_api_client.v2.model.create_feature_flag_data_type import CreateFeatureFlagDataType

        return {
            "attributes": (FeatureFlagAttributes,),
            "id": (UUID,),
            "type": (CreateFeatureFlagDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: FeatureFlagAttributes, id: UUID, type: CreateFeatureFlagDataType, **kwargs):
        """
        A feature flag resource.

        :param attributes: Attributes of a feature flag.
        :type attributes: FeatureFlagAttributes

        :param id: The unique identifier of the feature flag.
        :type id: UUID

        :param type: The resource type.
        :type type: CreateFeatureFlagDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
