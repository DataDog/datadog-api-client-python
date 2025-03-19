# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RetryStrategyLinear(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "interval": (str,),
            "max_retries": (float,),
        }

    attribute_map = {
        "interval": "interval",
        "max_retries": "maxRetries",
    }

    def __init__(self_, interval: str, max_retries: float, **kwargs):
        """
        The definition of ``RetryStrategyLinear`` object.

        :param interval: The ``RetryStrategyLinear`` ``interval``. The expected format is the number of seconds ending with an s. For example, 1 day is 86400s
        :type interval: str

        :param max_retries: The ``RetryStrategyLinear`` ``maxRetries``.
        :type max_retries: float
        """
        super().__init__(kwargs)

        self_.interval = interval
        self_.max_retries = max_retries
