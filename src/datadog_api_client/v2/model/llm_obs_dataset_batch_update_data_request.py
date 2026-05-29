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
    from datadog_api_client.v2.model.llm_obs_dataset_batch_update_data_attributes_request import (
        LLMObsDatasetBatchUpdateDataAttributesRequest,
    )
    from datadog_api_client.v2.model.llm_obs_dataset_type import LLMObsDatasetType


class LLMObsDatasetBatchUpdateDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_dataset_batch_update_data_attributes_request import (
            LLMObsDatasetBatchUpdateDataAttributesRequest,
        )
        from datadog_api_client.v2.model.llm_obs_dataset_type import LLMObsDatasetType

        return {
            "attributes": (LLMObsDatasetBatchUpdateDataAttributesRequest,),
            "id": (str,),
            "type": (LLMObsDatasetType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: LLMObsDatasetBatchUpdateDataAttributesRequest, id: str, type: LLMObsDatasetType, **kwargs
    ):
        """
        Data object for batch-updating records in an LLM Observability dataset.

        :param attributes: Attributes for batch-updating records in an LLM Observability dataset.
        :type attributes: LLMObsDatasetBatchUpdateDataAttributesRequest

        :param id: Unique identifier of the dataset.
        :type id: str

        :param type: Resource type of an LLM Observability dataset.
        :type type: LLMObsDatasetType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
