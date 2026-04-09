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
    from datadog_api_client.v2.model.llm_obs_annotated_interactions_data_attributes_response import (
        LLMObsAnnotatedInteractionsDataAttributesResponse,
    )
    from datadog_api_client.v2.model.llm_obs_annotated_interactions_type import LLMObsAnnotatedInteractionsType


class LLMObsAnnotatedInteractionsDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotated_interactions_data_attributes_response import (
            LLMObsAnnotatedInteractionsDataAttributesResponse,
        )
        from datadog_api_client.v2.model.llm_obs_annotated_interactions_type import LLMObsAnnotatedInteractionsType

        return {
            "attributes": (LLMObsAnnotatedInteractionsDataAttributesResponse,),
            "id": (str,),
            "type": (LLMObsAnnotatedInteractionsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: LLMObsAnnotatedInteractionsDataAttributesResponse,
        id: str,
        type: LLMObsAnnotatedInteractionsType,
        **kwargs,
    ):
        """
        Data object for annotated interactions.

        :param attributes: Attributes containing the list of annotated interactions.
        :type attributes: LLMObsAnnotatedInteractionsDataAttributesResponse

        :param id: The queue ID.
        :type id: str

        :param type: Resource type for annotated interactions.
        :type type: LLMObsAnnotatedInteractionsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
