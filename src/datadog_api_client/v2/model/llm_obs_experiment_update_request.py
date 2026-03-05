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
    from datadog_api_client.v2.model.llm_obs_experiment_update_data_request import LLMObsExperimentUpdateDataRequest


class LLMObsExperimentUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experiment_update_data_request import LLMObsExperimentUpdateDataRequest

        return {
            "data": (LLMObsExperimentUpdateDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsExperimentUpdateDataRequest, **kwargs):
        """
        Request to partially update an LLM Observability experiment.

        :param data: Data object for updating an LLM Observability experiment.
        :type data: LLMObsExperimentUpdateDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
