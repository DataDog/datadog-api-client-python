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
    from datadog_api_client.v2.model.rum_permanent_retention_filter_update_attributes import (
        RumPermanentRetentionFilterUpdateAttributes,
    )
    from datadog_api_client.v2.model.rum_permanent_retention_filter_type import RumPermanentRetentionFilterType


class RumPermanentRetentionFilterUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_permanent_retention_filter_update_attributes import (
            RumPermanentRetentionFilterUpdateAttributes,
        )
        from datadog_api_client.v2.model.rum_permanent_retention_filter_type import RumPermanentRetentionFilterType

        return {
            "attributes": (RumPermanentRetentionFilterUpdateAttributes,),
            "id": (str,),
            "type": (RumPermanentRetentionFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: RumPermanentRetentionFilterUpdateAttributes,
        id: str,
        type: RumPermanentRetentionFilterType,
        **kwargs,
    ):
        """
        The permanent retention filter properties to update.

        :param attributes: The attributes of a permanent retention filter that can be updated.
        :type attributes: RumPermanentRetentionFilterUpdateAttributes

        :param id: Permanent retention filter ID.
        :type id: str

        :param type: The resource type. The value must be ``permanent_retention_filters``.
        :type type: RumPermanentRetentionFilterType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
