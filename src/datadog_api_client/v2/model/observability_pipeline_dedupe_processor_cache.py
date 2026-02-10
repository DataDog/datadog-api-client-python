# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ObservabilityPipelineDedupeProcessorCache(ModelNormal):
    validations = {
        "num_events": {
            "inclusive_maximum": 1000000000,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "num_events": (int,),
        }

    attribute_map = {
        "num_events": "num_events",
    }

    def __init__(self_, num_events: int, **kwargs):
        """
        Configuration for the cache used to detect duplicates.

        :param num_events: The number of events to cache for duplicate detection.
        :type num_events: int
        """
        super().__init__(kwargs)

        self_.num_events = num_events
