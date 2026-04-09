# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ObservabilityPipelineEnrichmentTableFieldVrlLookup(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "vrl": (str,),
        }

    attribute_map = {
        "vrl": "vrl",
    }

    def __init__(self_, vrl: str, **kwargs):
        """
        Evaluates a VRL expression to produce the lookup key.

        :param vrl: A VRL expression that returns the value to use as the lookup key.
        :type vrl: str
        """
        super().__init__(kwargs)

        self_.vrl = vrl
