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
    from datadog_api_client.v2.model.completion_condition import CompletionCondition
    from datadog_api_client.v2.model.retry_strategy import RetryStrategy


class CompletionGate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.completion_condition import CompletionCondition
        from datadog_api_client.v2.model.retry_strategy import RetryStrategy

        return {
            "completion_condition": (CompletionCondition,),
            "retry_strategy": (RetryStrategy,),
        }

    attribute_map = {
        "completion_condition": "completionCondition",
        "retry_strategy": "retryStrategy",
    }

    def __init__(self_, completion_condition: CompletionCondition, retry_strategy: RetryStrategy, **kwargs):
        """
        Used to create conditions before running subsequent actions.

        :param completion_condition: The definition of ``CompletionCondition`` object.
        :type completion_condition: CompletionCondition

        :param retry_strategy: The definition of ``RetryStrategy`` object.
        :type retry_strategy: RetryStrategy
        """
        super().__init__(kwargs)

        self_.completion_condition = completion_condition
        self_.retry_strategy = retry_strategy
