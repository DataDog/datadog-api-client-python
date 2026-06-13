# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LLMObsPatternsTriggerRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "config_id": (str,),
        }

    attribute_map = {
        "config_id": "config_id",
    }

    def __init__(self_, config_id: str, **kwargs):
        """
        Attributes for triggering an LLM Observability patterns run.

        :param config_id: The ID of the patterns configuration to run.
        :type config_id: str
        """
        super().__init__(kwargs)

        self_.config_id = config_id
