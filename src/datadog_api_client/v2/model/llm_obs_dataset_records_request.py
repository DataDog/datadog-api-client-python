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
    from datadog_api_client.v2.model.llm_obs_dataset_records_data_request import LLMObsDatasetRecordsDataRequest


class LLMObsDatasetRecordsRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_dataset_records_data_request import LLMObsDatasetRecordsDataRequest

        return {
            "data": (LLMObsDatasetRecordsDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsDatasetRecordsDataRequest, **kwargs):
        """
        Request to append records to an LLM Observability dataset.

        :param data: Data object for appending records to an LLM Observability dataset.
        :type data: LLMObsDatasetRecordsDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
