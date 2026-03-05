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
    from datadog_api_client.v2.model.llm_obs_delete_experiments_data_request import LLMObsDeleteExperimentsDataRequest


class LLMObsDeleteExperimentsRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_delete_experiments_data_request import (
            LLMObsDeleteExperimentsDataRequest,
        )

        return {
            "data": (LLMObsDeleteExperimentsDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsDeleteExperimentsDataRequest, **kwargs):
        """
        Request to delete one or more LLM Observability experiments.

        :param data: Data object for deleting LLM Observability experiments.
        :type data: LLMObsDeleteExperimentsDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
