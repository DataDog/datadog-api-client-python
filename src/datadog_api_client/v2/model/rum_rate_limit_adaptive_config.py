# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RumRateLimitAdaptiveConfig(ModelNormal):
    validations = {
        "max_retention_rate": {
            "inclusive_maximum": 1,
            "exclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "max_retention_rate": (float,),
        }

    attribute_map = {
        "max_retention_rate": "max_retention_rate",
    }

    def __init__(self_, max_retention_rate: float, **kwargs):
        """
        The configuration used when ``mode`` is ``adaptive``.

        :param max_retention_rate: The maximum fraction of sessions to retain, in the range ``(0, 1]``.
        :type max_retention_rate: float
        """
        super().__init__(kwargs)

        self_.max_retention_rate = max_retention_rate
