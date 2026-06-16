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
    from datadog_api_client.v2.model.llm_obs_patterns_run_status_response_data import (
        LLMObsPatternsRunStatusResponseData,
    )


class LLMObsPatternsRunStatusResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_patterns_run_status_response_data import (
            LLMObsPatternsRunStatusResponseData,
        )

        return {
            "data": (LLMObsPatternsRunStatusResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsPatternsRunStatusResponseData, **kwargs):
        """
        Response containing the status of an LLM Observability patterns run.

        :param data: Data object of an LLM Observability patterns run status response.
        :type data: LLMObsPatternsRunStatusResponseData
        """
        super().__init__(kwargs)

        self_.data = data
