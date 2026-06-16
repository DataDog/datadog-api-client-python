# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LLMObsPatternsTriggerResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "config_id": (str,),
            "run_id": (str,),
            "status": (str,),
        }

    attribute_map = {
        "config_id": "config_id",
        "run_id": "run_id",
        "status": "status",
    }

    def __init__(self_, config_id: str, run_id: str, status: str, **kwargs):
        """
        Attributes of an LLM Observability patterns trigger response.

        :param config_id: The ID of the patterns configuration that was run.
        :type config_id: str

        :param run_id: The ID of the patterns run that was started.
        :type run_id: str

        :param status: Status of the patterns run.
        :type status: str
        """
        super().__init__(kwargs)

        self_.config_id = config_id
        self_.run_id = run_id
        self_.status = status
