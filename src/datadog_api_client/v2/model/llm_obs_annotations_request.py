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
    from datadog_api_client.v2.model.llm_obs_annotations_data_request import LLMObsAnnotationsDataRequest


class LLMObsAnnotationsRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotations_data_request import LLMObsAnnotationsDataRequest

        return {
            "data": (LLMObsAnnotationsDataRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsAnnotationsDataRequest, **kwargs):
        """
        Request to create or update annotations on interactions in an annotation queue.

        :param data: Data object for creating or updating annotations.
        :type data: LLMObsAnnotationsDataRequest
        """
        super().__init__(kwargs)

        self_.data = data
