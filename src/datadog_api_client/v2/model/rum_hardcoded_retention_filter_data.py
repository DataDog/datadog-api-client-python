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
    from datadog_api_client.v2.model.rum_hardcoded_retention_filter_attributes import (
        RumHardcodedRetentionFilterAttributes,
    )
    from datadog_api_client.v2.model.rum_hardcoded_retention_filter_meta import RumHardcodedRetentionFilterMeta
    from datadog_api_client.v2.model.rum_hardcoded_retention_filter_type import RumHardcodedRetentionFilterType


class RumHardcodedRetentionFilterData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_hardcoded_retention_filter_attributes import (
            RumHardcodedRetentionFilterAttributes,
        )
        from datadog_api_client.v2.model.rum_hardcoded_retention_filter_meta import RumHardcodedRetentionFilterMeta
        from datadog_api_client.v2.model.rum_hardcoded_retention_filter_type import RumHardcodedRetentionFilterType

        return {
            "attributes": (RumHardcodedRetentionFilterAttributes,),
            "id": (str,),
            "meta": (RumHardcodedRetentionFilterMeta,),
            "type": (RumHardcodedRetentionFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "meta": "meta",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[RumHardcodedRetentionFilterAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        meta: Union[RumHardcodedRetentionFilterMeta, UnsetType] = unset,
        type: Union[RumHardcodedRetentionFilterType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A hardcoded retention filter.

        :param attributes: The attributes of a hardcoded retention filter.
        :type attributes: RumHardcodedRetentionFilterAttributes, optional

        :param id: The ID of the hardcoded retention filter.
        :type id: str, optional

        :param meta: Metadata about the hardcoded retention filter.
        :type meta: RumHardcodedRetentionFilterMeta, optional

        :param type: The resource type. The value must be ``hardcoded_retention_filters``.
        :type type: RumHardcodedRetentionFilterType, optional
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
