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
    from datadog_api_client.v2.model.rum_permanent_retention_filter_meta import RumPermanentRetentionFilterMeta
    from datadog_api_client.v2.model.rum_permanent_retention_filter_type import RumPermanentRetentionFilterType


class RumPermanentRetentionFilterData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_permanent_retention_filter_attributes import (
            RumPermanentRetentionFilterAttributes,
        )
        from datadog_api_client.v2.model.rum_permanent_retention_filter_meta import RumPermanentRetentionFilterMeta
        from datadog_api_client.v2.model.rum_permanent_retention_filter_type import RumPermanentRetentionFilterType

        return {
            "attributes": (RumPermanentRetentionFilterAttributes,),
            "id": (str,),
            "meta": (RumPermanentRetentionFilterMeta,),
            "type": (RumPermanentRetentionFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "meta": "meta",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[RumPermanentRetentionFilterAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        meta: Union[RumPermanentRetentionFilterMeta, UnsetType] = unset,
        type: Union[RumPermanentRetentionFilterType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A permanent retention filter.

        :param attributes: The attributes of a permanent retention filter.
        :type attributes: RumPermanentRetentionFilterAttributes, optional

        :param id: Permanent retention filter ID.
        :type id: str, optional

        :param meta: Metadata about the permanent retention filter.
        :type meta: RumPermanentRetentionFilterMeta, optional

        :param type: The resource type. The value must be ``permanent_retention_filters``.
        :type type: RumPermanentRetentionFilterType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if meta is not unset:
            kwargs["meta"] = meta
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
