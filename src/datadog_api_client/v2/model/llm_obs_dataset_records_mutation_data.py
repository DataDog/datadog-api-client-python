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
    from datadog_api_client.v2.model.llm_obs_dataset_record_data_response import LLMObsDatasetRecordDataResponse


class LLMObsDatasetRecordsMutationData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_dataset_record_data_response import LLMObsDatasetRecordDataResponse

        return {
            "records": ([LLMObsDatasetRecordDataResponse],),
        }

    attribute_map = {
        "records": "records",
    }

    def __init__(self_, records: List[LLMObsDatasetRecordDataResponse], **kwargs):
        """
        Response containing records after a create or update operation.

        :param records: List of affected dataset records.
        :type records: [LLMObsDatasetRecordDataResponse]
        """
        super().__init__(kwargs)

        self_.records = records
