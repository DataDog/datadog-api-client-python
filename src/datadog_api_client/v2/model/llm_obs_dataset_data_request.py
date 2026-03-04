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
    from datadog_api_client.v2.model.llm_obs_dataset_data_attributes_request import LLMObsDatasetDataAttributesRequest
    from datadog_api_client.v2.model.llm_obs_dataset_type import LLMObsDatasetType


class LLMObsDatasetDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_dataset_data_attributes_request import (
            LLMObsDatasetDataAttributesRequest,
        )
        from datadog_api_client.v2.model.llm_obs_dataset_type import LLMObsDatasetType

        return {
            "attributes": (LLMObsDatasetDataAttributesRequest,),
            "type": (LLMObsDatasetType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: LLMObsDatasetDataAttributesRequest, type: LLMObsDatasetType, **kwargs):
        """
        Data object for creating an LLM Observability dataset.

        :param attributes: Attributes for creating an LLM Observability dataset.
        :type attributes: LLMObsDatasetDataAttributesRequest

        :param type: Resource type of an LLM Observability dataset.
        :type type: LLMObsDatasetType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
