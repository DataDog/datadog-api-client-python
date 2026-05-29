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
    from datadog_api_client.v2.model.rum_cross_product_sampling import RumCrossProductSampling
    from datadog_api_client.v2.model.rum_permanent_retention_filter_editability import (
        RumPermanentRetentionFilterEditability,
    )


class RumPermanentRetentionFilterAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_cross_product_sampling import RumCrossProductSampling
        from datadog_api_client.v2.model.rum_permanent_retention_filter_editability import (
            RumPermanentRetentionFilterEditability,
        )

        return {
            "cross_product_sampling": (RumCrossProductSampling,),
            "description": (str,),
            "editability": (RumPermanentRetentionFilterEditability,),
            "name": (str,),
        }

    attribute_map = {
        "cross_product_sampling": "cross_product_sampling",
        "description": "description",
        "editability": "editability",
        "name": "name",
    }

    def __init__(
        self_,
        cross_product_sampling: Union[RumCrossProductSampling, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        editability: Union[RumPermanentRetentionFilterEditability, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a permanent RUM retention filter.

        :param cross_product_sampling: The configuration for cross-product retention filters.
        :type cross_product_sampling: RumCrossProductSampling, optional

        :param description: A description of what the filter retains.
        :type description: str, optional

        :param editability: Indicates which cross-product fields of a permanent RUM retention filter can be updated.
        :type editability: RumPermanentRetentionFilterEditability, optional

        :param name: The display name of the permanent retention filter.
        :type name: str, optional
        """
        if cross_product_sampling is not unset:
            kwargs["cross_product_sampling"] = cross_product_sampling
        if description is not unset:
            kwargs["description"] = description
        if editability is not unset:
            kwargs["editability"] = editability
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
