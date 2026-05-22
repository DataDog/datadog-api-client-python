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
    from datadog_api_client.v2.model.llm_obs_dataset_draft_state_data_attributes import (
        LLMObsDatasetDraftStateDataAttributes,
    )
    from datadog_api_client.v2.model.llm_obs_dataset_draft_state_type import LLMObsDatasetDraftStateType


class LLMObsDatasetDraftStateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_dataset_draft_state_data_attributes import (
            LLMObsDatasetDraftStateDataAttributes,
        )
        from datadog_api_client.v2.model.llm_obs_dataset_draft_state_type import LLMObsDatasetDraftStateType

        return {
            "attributes": (LLMObsDatasetDraftStateDataAttributes,),
            "id": (str,),
            "type": (LLMObsDatasetDraftStateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: LLMObsDatasetDraftStateDataAttributes, id: str, type: LLMObsDatasetDraftStateType, **kwargs
    ):
        """
        Data object for an LLM Observability dataset draft state.

        :param attributes: Attributes of an LLM Observability dataset draft state.
        :type attributes: LLMObsDatasetDraftStateDataAttributes

        :param id: Unique identifier of the dataset draft state. Matches the dataset ID.
        :type id: str

        :param type: Resource type of an LLM Observability dataset draft state.
        :type type: LLMObsDatasetDraftStateType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
