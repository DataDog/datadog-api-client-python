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


class RumPermanentCrossProductSamplingUpdate(ModelNormal):
    validations = {
        "trace_sample_rate": {
            "inclusive_maximum": 100,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "trace_sample_rate": (float,),
        }

    attribute_map = {
        "trace_sample_rate": "trace_sample_rate",
    }

    def __init__(self_, trace_sample_rate: Union[float, UnsetType] = unset, **kwargs):
        """
        Partial update of the cross-product sample rates for a permanent retention filter.
        Only rates with a matching ``cross_product_sampling_editability`` flag set to ``true`` can be updated.

        :param trace_sample_rate: Percentage (0–100) of retained sessions (with ingested traces) whose traces are indexed.
            Omit to leave unchanged. Rejected if the filter's ``cross_product_sampling_editability.trace_sample_rate`` is ``false``.
        :type trace_sample_rate: float, optional
        """
        if trace_sample_rate is not unset:
            kwargs["trace_sample_rate"] = trace_sample_rate
        super().__init__(kwargs)
