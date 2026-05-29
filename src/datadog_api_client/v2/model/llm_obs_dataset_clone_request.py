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
    from datadog_api_client.v2.model.llm_obs_dataset_clone_data_request import LLMObsDatasetCloneDataRequest


class LLMObsDatasetCloneRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_dataset_clone_data_request import LLMObsDatasetCloneDataRequest

        return {
            "data": (LLMObsDatasetCloneDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsDatasetCloneDataRequest, **kwargs):
        """
        Request to clone an LLM Observability dataset.

        :param data: Data object for cloning an LLM Observability dataset.
        :type data: LLMObsDatasetCloneDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
