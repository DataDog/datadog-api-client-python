# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_dataset_data_response import LLMObsDatasetDataResponse
    from datadog_api_client.v2.model.llm_obs_cursor_meta import LLMObsCursorMeta


class LLMObsDatasetsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_dataset_data_response import LLMObsDatasetDataResponse
        from datadog_api_client.v2.model.llm_obs_cursor_meta import LLMObsCursorMeta

        return {
            "data": ([LLMObsDatasetDataResponse],),
            "meta": (LLMObsCursorMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_, data: List[LLMObsDatasetDataResponse], meta: Union[LLMObsCursorMeta, UnsetType] = unset, **kwargs
    ):
        """
        Response containing a list of LLM Observability datasets.

        :param data: List of datasets.
        :type data: [LLMObsDatasetDataResponse]

        :param meta: Pagination cursor metadata.
        :type meta: LLMObsCursorMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
