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
    from datadog_api_client.v2.model.retry_strategy import RetryStrategy


class ErrorHandler(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.retry_strategy import RetryStrategy

        return {
            "fallback_step_name": (str,),
            "retry_strategy": (RetryStrategy,),
        }

    attribute_map = {
        "fallback_step_name": "fallbackStepName",
        "retry_strategy": "retryStrategy",
    }

    def __init__(self_, fallback_step_name: str, retry_strategy: RetryStrategy, **kwargs):
        """
        Used to handle errors in an action.

        :param fallback_step_name: The ``ErrorHandler`` ``fallbackStepName``.
        :type fallback_step_name: str

        :param retry_strategy: The definition of ``RetryStrategy`` object.
        :type retry_strategy: RetryStrategy
        """
        super().__init__(kwargs)

        self_.fallback_step_name = fallback_step_name
        self_.retry_strategy = retry_strategy
