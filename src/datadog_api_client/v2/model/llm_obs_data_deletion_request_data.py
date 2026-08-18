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
    from datadog_api_client.v2.model.llm_obs_data_deletion_request_attributes import LLMObsDataDeletionRequestAttributes
    from datadog_api_client.v2.model.llm_obs_data_deletion_request_type import LLMObsDataDeletionRequestType


class LLMObsDataDeletionRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_data_deletion_request_attributes import (
            LLMObsDataDeletionRequestAttributes,
        )
        from datadog_api_client.v2.model.llm_obs_data_deletion_request_type import LLMObsDataDeletionRequestType

        return {
            "attributes": (LLMObsDataDeletionRequestAttributes,),
            "type": (LLMObsDataDeletionRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: LLMObsDataDeletionRequestAttributes, type: LLMObsDataDeletionRequestType, **kwargs):
        """
        Data object for an LLM Observability data deletion request.

        :param attributes: Attributes for an LLM Observability data deletion request.
        :type attributes: LLMObsDataDeletionRequestAttributes

        :param type: Resource type for an LLM Observability data deletion request.
        :type type: LLMObsDataDeletionRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
