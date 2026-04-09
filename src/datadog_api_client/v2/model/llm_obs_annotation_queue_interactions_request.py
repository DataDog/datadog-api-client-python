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
    from datadog_api_client.v2.model.llm_obs_annotation_queue_interactions_data_request import (
        LLMObsAnnotationQueueInteractionsDataRequest,
    )


class LLMObsAnnotationQueueInteractionsRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotation_queue_interactions_data_request import (
            LLMObsAnnotationQueueInteractionsDataRequest,
        )

        return {
            "data": (LLMObsAnnotationQueueInteractionsDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsAnnotationQueueInteractionsDataRequest, **kwargs):
        """
        Request to add interactions to an LLM Observability annotation queue.

        :param data: Data object for adding interactions to an annotation queue.
        :type data: LLMObsAnnotationQueueInteractionsDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
