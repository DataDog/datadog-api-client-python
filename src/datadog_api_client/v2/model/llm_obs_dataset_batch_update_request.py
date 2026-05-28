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
    from datadog_api_client.v2.model.llm_obs_dataset_batch_update_data_request import (
        LLMObsDatasetBatchUpdateDataRequest,
    )


class LLMObsDatasetBatchUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_dataset_batch_update_data_request import (
            LLMObsDatasetBatchUpdateDataRequest,
        )

        return {
            "data": (LLMObsDatasetBatchUpdateDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsDatasetBatchUpdateDataRequest, **kwargs):
        """
        Request to batch-insert, update, and delete records in an LLM Observability dataset.

        :param data: Data object for batch-updating records in an LLM Observability dataset.
        :type data: LLMObsDatasetBatchUpdateDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
