# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.retry_strategy_kind import RetryStrategyKind
    from datadog_api_client.v2.model.retry_strategy_linear import RetryStrategyLinear


class RetryStrategy(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.retry_strategy_kind import RetryStrategyKind
        from datadog_api_client.v2.model.retry_strategy_linear import RetryStrategyLinear

        return {
            "kind": (RetryStrategyKind,),
            "linear": (RetryStrategyLinear,),
        }

    attribute_map = {
        "kind": "kind",
        "linear": "linear",
    }

    def __init__(self_, kind: RetryStrategyKind, linear: RetryStrategyLinear, **kwargs):
        """
        The definition of ``RetryStrategy`` object.

        :param kind: The definition of ``RetryStrategyKind`` object.
        :type kind: RetryStrategyKind

        :param linear: The definition of ``RetryStrategyLinear`` object.
        :type linear: RetryStrategyLinear
        """
        super().__init__(kwargs)

        self_.kind = kind
        self_.linear = linear
