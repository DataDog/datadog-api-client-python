# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_permanent_retention_filter_attributes import (
        RumPermanentRetentionFilterAttributes,
    )
    from datadog_api_client.v2.model.rum_permanent_retention_filter_id import RumPermanentRetentionFilterID
    from datadog_api_client.v2.model.rum_permanent_retention_filter_type import RumPermanentRetentionFilterType


class RumPermanentRetentionFilterData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_permanent_retention_filter_attributes import (
            RumPermanentRetentionFilterAttributes,
        )
        from datadog_api_client.v2.model.rum_permanent_retention_filter_id import RumPermanentRetentionFilterID
        from datadog_api_client.v2.model.rum_permanent_retention_filter_type import RumPermanentRetentionFilterType

        return {
            "attributes": (RumPermanentRetentionFilterAttributes,),
            "id": (RumPermanentRetentionFilterID,),
            "type": (RumPermanentRetentionFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[RumPermanentRetentionFilterAttributes, UnsetType] = unset,
        id: Union[RumPermanentRetentionFilterID, UnsetType] = unset,
        type: Union[RumPermanentRetentionFilterType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A permanent RUM retention filter.

        :param attributes: The attributes of a permanent RUM retention filter.
        :type attributes: RumPermanentRetentionFilterAttributes, optional

        :param id: The identifier of a permanent RUM retention filter.
        :type id: RumPermanentRetentionFilterID, optional

        :param type: The type of the resource. The value should always be ``permanent_retention_filters``.
        :type type: RumPermanentRetentionFilterType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
