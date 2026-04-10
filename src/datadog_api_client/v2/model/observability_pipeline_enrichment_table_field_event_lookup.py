# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ObservabilityPipelineEnrichmentTableFieldEventLookup(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "event": (str,),
        }

    attribute_map = {
        "event": "event",
    }

    def __init__(self_, event: str, **kwargs):
        """
        Looks up a value from a field path in the log event.

        :param event: The path to the field in the log event to use as the lookup key.
        :type event: str
        """
        super().__init__(kwargs)

        self_.event = event
