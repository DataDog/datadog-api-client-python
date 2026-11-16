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
    from datadog_api_client.v2.model.ai_gateway_rate_limit_window_limit_metric import (
        AiGatewayRateLimitWindowLimitMetric,
    )
    from datadog_api_client.v2.model.ai_gateway_rate_limit_window_limit_window import (
        AiGatewayRateLimitWindowLimitWindow,
    )


class AiGatewayRateLimitWindowLimit(ModelNormal):
    validations = {
        "amount": {
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_rate_limit_window_limit_metric import (
            AiGatewayRateLimitWindowLimitMetric,
        )
        from datadog_api_client.v2.model.ai_gateway_rate_limit_window_limit_window import (
            AiGatewayRateLimitWindowLimitWindow,
        )

        return {
            "amount": (int,),
            "metric": (AiGatewayRateLimitWindowLimitMetric,),
            "window": (AiGatewayRateLimitWindowLimitWindow,),
        }

    attribute_map = {
        "amount": "amount",
        "metric": "metric",
        "window": "window",
    }

    def __init__(
        self_,
        amount: int,
        metric: AiGatewayRateLimitWindowLimitMetric,
        window: AiGatewayRateLimitWindowLimitWindow,
        **kwargs,
    ):
        """
        A limit on one metric over a rolling window longer than a minute.

        :param amount: Maximum amount of the metric over the window. For ``cost`` , the amount is priced spend in microcents of 1e-8 USD each, as in ``cost_microcents_per_minute``. For the same metric, a longer window must have a larger amount.
        :type amount: int

        :param metric: The metric that a window limit counts. ``cost`` counts priced spend in microcents.
        :type metric: AiGatewayRateLimitWindowLimitMetric

        :param window: The rolling window that a limit applies to. For per-minute limits, use the ``*_per_minute`` fields instead.
        :type window: AiGatewayRateLimitWindowLimitWindow
        """
        super().__init__(kwargs)

        self_.amount = amount
        self_.metric = metric
        self_.window = window
