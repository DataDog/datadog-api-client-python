# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RumRecoveryCountResponseAttributes(ModelNormal):
    validations = {
        "estimated_count": {
            "inclusive_minimum": 0,
        },
        "max_recoverable_sessions": {
            "inclusive_maximum": 2147483647,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "estimated_count": (int,),
            "max_recoverable_sessions": (int,),
        }

    attribute_map = {
        "estimated_count": "estimated_count",
        "max_recoverable_sessions": "max_recoverable_sessions",
    }

    def __init__(self_, estimated_count: int, max_recoverable_sessions: int, **kwargs):
        """
        Approximate recoverable count.

        :param estimated_count: Estimated distinct recoverable sessions not already retained in hot storage. The full estimate is returned without capping it at max_recoverable_sessions.
        :type estimated_count: int

        :param max_recoverable_sessions: Configured maximum estimated recoverable sessions per batch (100,000 by default). Estimates equal to this value are accepted at creation.
        :type max_recoverable_sessions: int
        """
        super().__init__(kwargs)

        self_.estimated_count = estimated_count
        self_.max_recoverable_sessions = max_recoverable_sessions
