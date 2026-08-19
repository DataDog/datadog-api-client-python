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
    from datadog_api_client.v2.model.rum_exclusion_filter_update_attributes import RumExclusionFilterUpdateAttributes
    from datadog_api_client.v2.model.rum_exclusion_filter_type import RumExclusionFilterType


class RumExclusionFilterUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_exclusion_filter_update_attributes import (
            RumExclusionFilterUpdateAttributes,
        )
        from datadog_api_client.v2.model.rum_exclusion_filter_type import RumExclusionFilterType

        return {
            "attributes": (RumExclusionFilterUpdateAttributes,),
            "id": (str,),
            "type": (RumExclusionFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: RumExclusionFilterUpdateAttributes, id: str, type: RumExclusionFilterType, **kwargs
    ):
        """
        The exclusion filter properties to update.

        :param attributes: The attributes of an exclusion filter that can be updated.
            For the built-in Error Tracking exclusion filter, only ``enabled`` can be set;
            ``name`` , ``event_type`` , and ``query`` must be omitted.
        :type attributes: RumExclusionFilterUpdateAttributes

        :param id: The ID of the exclusion filter. Must match the ``ef_id`` path parameter.
        :type id: str

        :param type: The resource type. The value must be ``exclusion_filters``.
        :type type: RumExclusionFilterType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
