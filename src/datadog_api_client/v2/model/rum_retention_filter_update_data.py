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
    from datadog_api_client.v2.model.rum_retention_filter_update_attributes import RumRetentionFilterUpdateAttributes
    from datadog_api_client.v2.model.rum_retention_filter_type import RumRetentionFilterType


class RumRetentionFilterUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_retention_filter_update_attributes import (
            RumRetentionFilterUpdateAttributes,
        )
        from datadog_api_client.v2.model.rum_retention_filter_type import RumRetentionFilterType

        return {
            "attributes": (RumRetentionFilterUpdateAttributes,),
            "id": (str,),
            "type": (RumRetentionFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: RumRetentionFilterUpdateAttributes, id: str, type: RumRetentionFilterType, **kwargs
    ):
        """
        The new RUM retention filter properties to update.

        :param attributes: The object describing attributes of a RUM retention filter to update.
        :type attributes: RumRetentionFilterUpdateAttributes

        :param id: ID of retention filter in UUID.
        :type id: str

        :param type: The type of the resource. The value should always be retention_filters.
        :type type: RumRetentionFilterType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
