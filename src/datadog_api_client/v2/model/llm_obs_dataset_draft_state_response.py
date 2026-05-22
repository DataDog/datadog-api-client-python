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
    from datadog_api_client.v2.model.llm_obs_dataset_draft_state_data import LLMObsDatasetDraftStateData


class LLMObsDatasetDraftStateResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_dataset_draft_state_data import LLMObsDatasetDraftStateData

        return {
            "data": (LLMObsDatasetDraftStateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsDatasetDraftStateData, **kwargs):
        """
        Response containing the draft state of an LLM Observability dataset.

        :param data: Data object for an LLM Observability dataset draft state.
        :type data: LLMObsDatasetDraftStateData
        """
        super().__init__(kwargs)

        self_.data = data
