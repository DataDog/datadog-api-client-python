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
    from datadog_api_client.v2.model.llm_obs_delete_annotations_data_response import LLMObsDeleteAnnotationsDataResponse


class LLMObsDeleteAnnotationsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_delete_annotations_data_response import (
            LLMObsDeleteAnnotationsDataResponse,
        )

        return {
            "data": (LLMObsDeleteAnnotationsDataResponse,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: LLMObsDeleteAnnotationsDataResponse, **kwargs):
        """
        Response for a batch annotation deletion. Partial errors are listed in the
        response if any annotations could not be deleted.

        :param data: Data object for the annotation deletion response.
        :type data: LLMObsDeleteAnnotationsDataResponse
        """
        super().__init__(kwargs)

        self_.data = data
