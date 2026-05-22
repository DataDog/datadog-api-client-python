# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_dataset_version_data import LLMObsDatasetVersionData


class LLMObsDatasetVersionsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_dataset_version_data import LLMObsDatasetVersionData

        return {
            "data": ([LLMObsDatasetVersionData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[LLMObsDatasetVersionData], **kwargs):
        """
        Response containing the active versions of an LLM Observability dataset.

        :param data: List of dataset versions.
        :type data: [LLMObsDatasetVersionData]
        """
        super().__init__(kwargs)

        self_.data = data
