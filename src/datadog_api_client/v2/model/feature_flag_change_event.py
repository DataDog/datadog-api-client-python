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
    from datadog_api_client.v2.model.feature_flag_change_event_attributes import FeatureFlagChangeEventAttributes
    from datadog_api_client.v2.model.feature_flag_change_event_type import FeatureFlagChangeEventType


class FeatureFlagChangeEvent(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.feature_flag_change_event_attributes import FeatureFlagChangeEventAttributes
        from datadog_api_client.v2.model.feature_flag_change_event_type import FeatureFlagChangeEventType

        return {
            "attributes": (FeatureFlagChangeEventAttributes,),
            "id": (UUID,),
            "type": (FeatureFlagChangeEventType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: FeatureFlagChangeEventAttributes, id: UUID, type: FeatureFlagChangeEventType, **kwargs
    ):
        """
        A change made to a feature flag.

        :param attributes: Attributes of a feature flag change event.
        :type attributes: FeatureFlagChangeEventAttributes

        :param id: The ID of the change event.
        :type id: UUID

        :param type: The resource type.
        :type type: FeatureFlagChangeEventType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
