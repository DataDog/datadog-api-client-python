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
    from datadog_api_client.v2.model.llm_obs_dataset_version_data_attributes import LLMObsDatasetVersionDataAttributes
    from datadog_api_client.v2.model.llm_obs_dataset_version_type import LLMObsDatasetVersionType


class LLMObsDatasetVersionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_dataset_version_data_attributes import (
            LLMObsDatasetVersionDataAttributes,
        )
        from datadog_api_client.v2.model.llm_obs_dataset_version_type import LLMObsDatasetVersionType

        return {
            "attributes": (LLMObsDatasetVersionDataAttributes,),
            "id": (str,),
            "type": (LLMObsDatasetVersionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: LLMObsDatasetVersionDataAttributes, id: str, type: LLMObsDatasetVersionType, **kwargs
    ):
        """
        Data object for an LLM Observability dataset version.

        :param attributes: Attributes of an LLM Observability dataset version.
        :type attributes: LLMObsDatasetVersionDataAttributes

        :param id: Unique identifier of the dataset version.
        :type id: str

        :param type: Resource type of an LLM Observability dataset version.
        :type type: LLMObsDatasetVersionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
