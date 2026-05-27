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
    from datadog_api_client.v2.model.rum_permanent_cross_product_sampling_update import (
        RumPermanentCrossProductSamplingUpdate,
    )


class RumPermanentRetentionFilterUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_permanent_cross_product_sampling_update import (
            RumPermanentCrossProductSamplingUpdate,
        )

        return {
            "cross_product_sampling": (RumPermanentCrossProductSamplingUpdate,),
        }

    attribute_map = {
        "cross_product_sampling": "cross_product_sampling",
    }

    def __init__(
        self_, cross_product_sampling: Union[RumPermanentCrossProductSamplingUpdate, UnsetType] = unset, **kwargs
    ):
        """
        The attributes of a permanent retention filter that can be updated.

        :param cross_product_sampling: Partial update of the cross-product sample rates for a permanent retention filter.
            Only rates with a matching ``cross_product_sampling_editability`` flag set to ``true`` can be updated.
        :type cross_product_sampling: RumPermanentCrossProductSamplingUpdate, optional
        """
        if cross_product_sampling is not unset:
            kwargs["cross_product_sampling"] = cross_product_sampling
        super().__init__(kwargs)
