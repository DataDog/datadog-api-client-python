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
    from datadog_api_client.v2.model.llm_obs_delete_datasets_data_attributes_request import (
        LLMObsDeleteDatasetsDataAttributesRequest,
    )
    from datadog_api_client.v2.model.llm_obs_dataset_type import LLMObsDatasetType


class LLMObsDeleteDatasetsDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_delete_datasets_data_attributes_request import (
            LLMObsDeleteDatasetsDataAttributesRequest,
        )
        from datadog_api_client.v2.model.llm_obs_dataset_type import LLMObsDatasetType

        return {
            "attributes": (LLMObsDeleteDatasetsDataAttributesRequest,),
            "type": (LLMObsDatasetType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: LLMObsDeleteDatasetsDataAttributesRequest, type: LLMObsDatasetType, **kwargs):
        """
        Data object for deleting LLM Observability datasets.

        :param attributes: Attributes for deleting LLM Observability datasets.
        :type attributes: LLMObsDeleteDatasetsDataAttributesRequest

        :param type: Resource type of an LLM Observability dataset.
        :type type: LLMObsDatasetType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
