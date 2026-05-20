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
    from datadog_api_client.v2.model.llm_obs_data_deletion_request_data import LLMObsDataDeletionRequestData


class LLMObsDataDeletionRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_data_deletion_request_data import LLMObsDataDeletionRequestData

        return {
            "data": (LLMObsDataDeletionRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsDataDeletionRequestData, **kwargs):
        """
        Request to delete LLM Observability data.

        :param data: Data object for an LLM Observability data deletion request.
        :type data: LLMObsDataDeletionRequestData
        """
        super().__init__(kwargs)

        self_.data = data
