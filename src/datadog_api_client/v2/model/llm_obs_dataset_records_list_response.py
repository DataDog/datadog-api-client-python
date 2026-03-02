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
    from datadog_api_client.v2.model.llm_obs_dataset_record_data_response import LLMObsDatasetRecordDataResponse
    from datadog_api_client.v2.model.llm_obs_cursor_meta import LLMObsCursorMeta


class LLMObsDatasetRecordsListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_dataset_record_data_response import LLMObsDatasetRecordDataResponse
        from datadog_api_client.v2.model.llm_obs_cursor_meta import LLMObsCursorMeta

        return {
            "data": ([LLMObsDatasetRecordDataResponse],),
            "meta": (LLMObsCursorMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_, data: List[LLMObsDatasetRecordDataResponse], meta: Union[LLMObsCursorMeta, UnsetType] = unset, **kwargs
    ):
        """
        Response containing a paginated list of LLM Observability dataset records.

        :param data: List of dataset records.
        :type data: [LLMObsDatasetRecordDataResponse]

        :param meta: Pagination cursor metadata.
        :type meta: LLMObsCursorMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
