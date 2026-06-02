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
    from datadog_api_client.v2.model.rum_hardcoded_cross_product_sampling_update import (
        RumHardcodedCrossProductSamplingUpdate,
    )


class RumHardcodedRetentionFilterUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_hardcoded_cross_product_sampling_update import (
            RumHardcodedCrossProductSamplingUpdate,
        )

        return {
            "cross_product_sampling": (RumHardcodedCrossProductSamplingUpdate,),
        }

    attribute_map = {
        "cross_product_sampling": "cross_product_sampling",
    }

    def __init__(
        self_, cross_product_sampling: Union[RumHardcodedCrossProductSamplingUpdate, UnsetType] = unset, **kwargs
    ):
        """
        The attributes of a hardcoded retention filter that can be updated.
        Only fields whose matching flag in ``cross_product_sampling_editability`` is ``true`` can be modified.

        :param cross_product_sampling: Partial update for cross-product retention of a hardcoded retention filter.
            Only fields whose matching flag in ``cross_product_sampling_editability`` is ``true`` can be updated.
        :type cross_product_sampling: RumHardcodedCrossProductSamplingUpdate, optional
        """
        if cross_product_sampling is not unset:
            kwargs["cross_product_sampling"] = cross_product_sampling
        super().__init__(kwargs)
