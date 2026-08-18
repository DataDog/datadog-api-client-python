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
    from datadog_api_client.v2.model.rum_exclusion_filter_create_attributes import RumExclusionFilterCreateAttributes
    from datadog_api_client.v2.model.rum_exclusion_filter_type import RumExclusionFilterType


class RumExclusionFilterCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_exclusion_filter_create_attributes import (
            RumExclusionFilterCreateAttributes,
        )
        from datadog_api_client.v2.model.rum_exclusion_filter_type import RumExclusionFilterType

        return {
            "attributes": (RumExclusionFilterCreateAttributes,),
            "type": (RumExclusionFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: RumExclusionFilterCreateAttributes, type: RumExclusionFilterType, **kwargs):
        """
        The new exclusion filter properties to create.

        :param attributes: The attributes of an exclusion filter to create.
        :type attributes: RumExclusionFilterCreateAttributes

        :param type: The resource type. The value must be ``exclusion_filters``.
        :type type: RumExclusionFilterType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
