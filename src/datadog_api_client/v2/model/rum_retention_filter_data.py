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
    from datadog_api_client.v2.model.rum_retention_filter_attributes import RUMRetentionFilterAttributes
    from datadog_api_client.v2.model.rum_retention_filter_meta import RUMRetentionFilterMeta
    from datadog_api_client.v2.model.rum_retention_filter_type import RUMRetentionFilterType


class RUMRetentionFilterData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_retention_filter_attributes import RUMRetentionFilterAttributes
        from datadog_api_client.v2.model.rum_retention_filter_meta import RUMRetentionFilterMeta
        from datadog_api_client.v2.model.rum_retention_filter_type import RUMRetentionFilterType

        return {
            "attributes": (RUMRetentionFilterAttributes,),
            "id": (str,),
            "meta": (RUMRetentionFilterMeta,),
            "type": (RUMRetentionFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "meta": "meta",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[RUMRetentionFilterAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        meta: Union[RUMRetentionFilterMeta, UnsetType] = unset,
        type: Union[RUMRetentionFilterType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The RUM retention filter.

        :param attributes: The object describing attributes of a RUM retention filter.
        :type attributes: RUMRetentionFilterAttributes, optional

        :param id: ID of retention filter in UUID.
        :type id: str, optional

        :param meta: Metadata about the retention filter.
        :type meta: RUMRetentionFilterMeta, optional

        :param type: The type of the resource. The value should always be retention_filters.
        :type type: RUMRetentionFilterType, optional
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
