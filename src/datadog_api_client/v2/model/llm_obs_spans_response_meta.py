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
    from datadog_api_client.v2.model.llm_obs_spans_response_page import LLMObsSpansResponsePage


class LLMObsSpansResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_spans_response_page import LLMObsSpansResponsePage

        return {
            "elapsed": (int,),
            "page": (LLMObsSpansResponsePage,),
            "request_id": (str,),
            "status": (str,),
        }

    attribute_map = {
        "elapsed": "elapsed",
        "page": "page",
        "request_id": "request_id",
        "status": "status",
    }

    def __init__(self_, elapsed: int, page: LLMObsSpansResponsePage, request_id: str, status: str, **kwargs):
        """
        Metadata accompanying the spans response.

        :param elapsed: Time elapsed for the query in milliseconds.
        :type elapsed: int

        :param page: Pagination cursor for the spans response.
        :type page: LLMObsSpansResponsePage

        :param request_id: Unique identifier for the request.
        :type request_id: str

        :param status: Status of the query execution.
        :type status: str
        """
        super().__init__(kwargs)

        self_.elapsed = elapsed
        self_.page = page
        self_.request_id = request_id
        self_.status = status
