# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.score_response_data import ScoreResponseData
    from datadog_api_client.v2.model.paginated_response_meta import PaginatedResponseMeta


class ListScoresResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.score_response_data import ScoreResponseData
        from datadog_api_client.v2.model.paginated_response_meta import PaginatedResponseMeta

        return {
            "data": ([ScoreResponseData],),
            "meta": (PaginatedResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[ScoreResponseData], meta: PaginatedResponseMeta, **kwargs):
        """
        Response containing a list of scores.

        :param data: Array of scores.
        :type data: [ScoreResponseData]

        :param meta: Metadata for scores response.
        :type meta: PaginatedResponseMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
