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
    from datadog_api_client.v2.model.rum_retention_filter_create_attributes import RumRetentionFilterCreateAttributes
    from datadog_api_client.v2.model.rum_retention_filter_meta import RumRetentionFilterMeta
    from datadog_api_client.v2.model.rum_retention_filter_type import RumRetentionFilterType


class RumRetentionFilterCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_retention_filter_create_attributes import (
            RumRetentionFilterCreateAttributes,
        )
        from datadog_api_client.v2.model.rum_retention_filter_meta import RumRetentionFilterMeta
        from datadog_api_client.v2.model.rum_retention_filter_type import RumRetentionFilterType

        return {
            "attributes": (RumRetentionFilterCreateAttributes,),
            "meta": (RumRetentionFilterMeta,),
            "type": (RumRetentionFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "meta": "meta",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: RumRetentionFilterCreateAttributes,
        type: RumRetentionFilterType,
        meta: Union[RumRetentionFilterMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        The new RUM retention filter properties to create.

        :param attributes: The object describing attributes of a RUM retention filter to create.
        :type attributes: RumRetentionFilterCreateAttributes

        :param meta: The object describing metadata of a RUM retention filter.
        :type meta: RumRetentionFilterMeta, optional

        :param type: The type of the resource. The value should always be retention_filters.
        :type type: RumRetentionFilterType
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
