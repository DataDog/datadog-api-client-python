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
    from datadog_api_client.v2.model.llm_obs_delete_datasets_data_request import LLMObsDeleteDatasetsDataRequest


class LLMObsDeleteDatasetsRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_delete_datasets_data_request import LLMObsDeleteDatasetsDataRequest

        return {
            "data": (LLMObsDeleteDatasetsDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsDeleteDatasetsDataRequest, **kwargs):
        """
        Request to delete one or more LLM Observability datasets.

        :param data: Data object for deleting LLM Observability datasets.
        :type data: LLMObsDeleteDatasetsDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
