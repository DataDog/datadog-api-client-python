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
    from datadog_api_client.v2.model.rum_exclusion_filter_attributes import RumExclusionFilterAttributes
    from datadog_api_client.v2.model.rum_exclusion_filter_meta import RumExclusionFilterMeta
    from datadog_api_client.v2.model.rum_exclusion_filter_type import RumExclusionFilterType


class RumExclusionFilterData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_exclusion_filter_attributes import RumExclusionFilterAttributes
        from datadog_api_client.v2.model.rum_exclusion_filter_meta import RumExclusionFilterMeta
        from datadog_api_client.v2.model.rum_exclusion_filter_type import RumExclusionFilterType

        return {
            "attributes": (RumExclusionFilterAttributes,),
            "id": (str,),
            "meta": (RumExclusionFilterMeta,),
            "type": (RumExclusionFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "meta": "meta",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: RumExclusionFilterType,
        attributes: Union[RumExclusionFilterAttributes, UnsetType] = unset,
        meta: Union[RumExclusionFilterMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        An exclusion filter.

        :param attributes: The attributes of an exclusion filter.
        :type attributes: RumExclusionFilterAttributes, optional

        :param id: The ID of the exclusion filter.
        :type id: str

        :param meta: Metadata about the exclusion filter.
        :type meta: RumExclusionFilterMeta, optional

        :param type: The resource type. The value must be ``exclusion_filters``.
        :type type: RumExclusionFilterType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
