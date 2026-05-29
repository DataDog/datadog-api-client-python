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
    from datadog_api_client.v2.model.rum_cross_product_sampling_update import RumCrossProductSamplingUpdate


class RumPermanentRetentionFilterUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_cross_product_sampling_update import RumCrossProductSamplingUpdate

        return {
            "cross_product_sampling": (RumCrossProductSamplingUpdate,),
        }

    attribute_map = {
        "cross_product_sampling": "cross_product_sampling",
    }

    def __init__(self_, cross_product_sampling: Union[RumCrossProductSamplingUpdate, UnsetType] = unset, **kwargs):
        """
        The configuration to update on a permanent RUM retention filter.

        :param cross_product_sampling: The configuration for cross-product retention filters. All fields are optional for partial updates.
        :type cross_product_sampling: RumCrossProductSamplingUpdate, optional
        """
        if cross_product_sampling is not unset:
            kwargs["cross_product_sampling"] = cross_product_sampling
        super().__init__(kwargs)
