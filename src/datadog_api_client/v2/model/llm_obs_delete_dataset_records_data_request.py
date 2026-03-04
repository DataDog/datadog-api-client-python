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
    from datadog_api_client.v2.model.llm_obs_delete_dataset_records_data_attributes_request import (
        LLMObsDeleteDatasetRecordsDataAttributesRequest,
    )
    from datadog_api_client.v2.model.llm_obs_record_type import LLMObsRecordType


class LLMObsDeleteDatasetRecordsDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_delete_dataset_records_data_attributes_request import (
            LLMObsDeleteDatasetRecordsDataAttributesRequest,
        )
        from datadog_api_client.v2.model.llm_obs_record_type import LLMObsRecordType

        return {
            "attributes": (LLMObsDeleteDatasetRecordsDataAttributesRequest,),
            "type": (LLMObsRecordType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: LLMObsDeleteDatasetRecordsDataAttributesRequest, type: LLMObsRecordType, **kwargs):
        """
        Data object for deleting records from an LLM Observability dataset.

        :param attributes: Attributes for deleting records from an LLM Observability dataset.
        :type attributes: LLMObsDeleteDatasetRecordsDataAttributesRequest

        :param type: Resource type of LLM Observability dataset records.
        :type type: LLMObsRecordType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
