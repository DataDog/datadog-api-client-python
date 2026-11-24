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
        RUMPermanentRetentionFilterAttributes,
    )
    from datadog_api_client.v2.model.rum_permanent_retention_filter_id import RUMPermanentRetentionFilterID
    from datadog_api_client.v2.model.rum_permanent_retention_filter_type import RUMPermanentRetentionFilterType


class RUMPermanentRetentionFilterData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_permanent_retention_filter_attributes import (
            RUMPermanentRetentionFilterAttributes,
        )
        from datadog_api_client.v2.model.rum_permanent_retention_filter_id import RUMPermanentRetentionFilterID
        from datadog_api_client.v2.model.rum_permanent_retention_filter_type import RUMPermanentRetentionFilterType

        return {
            "attributes": (RUMPermanentRetentionFilterAttributes,),
            "id": (RUMPermanentRetentionFilterID,),
            "type": (RUMPermanentRetentionFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[RUMPermanentRetentionFilterAttributes, UnsetType] = unset,
        id: Union[RUMPermanentRetentionFilterID, UnsetType] = unset,
        type: Union[RUMPermanentRetentionFilterType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A permanent RUM retention filter.

        :param attributes: The attributes of a permanent RUM retention filter.
        :type attributes: RUMPermanentRetentionFilterAttributes, optional

        :param id: The identifier of a permanent RUM retention filter.
        :type id: RUMPermanentRetentionFilterID, optional

        :param type: The type of the resource. The value should always be ``permanent_retention_filters``.
        :type type: RUMPermanentRetentionFilterType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
