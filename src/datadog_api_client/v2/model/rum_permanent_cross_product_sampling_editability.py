# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class RumPermanentCrossProductSamplingEditability(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "trace_sample_rate": (bool,),
        }

    attribute_map = {
        "trace_sample_rate": "trace_sample_rate",
    }

    def __init__(self_, trace_sample_rate: Union[bool, UnsetType] = unset, **kwargs):
        """
        Flags indicating which ``cross_product_sampling`` rates can be updated for this filter. Read-only.

        :param trace_sample_rate: If ``true`` , ``cross_product_sampling.trace_sample_rate`` can be updated on this filter.
        :type trace_sample_rate: bool, optional
        """
        if trace_sample_rate is not unset:
            kwargs["trace_sample_rate"] = trace_sample_rate
        super().__init__(kwargs)
