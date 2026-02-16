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
    from datadog_api_client.v2.model.action_match import ActionMatch


class PickActionResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.action_match import ActionMatch

        return {
            "matches": ([ActionMatch],),
            "request_id": (str,),
            "total_matches": (int,),
        }

    attribute_map = {
        "matches": "matches",
        "request_id": "request_id",
        "total_matches": "total_matches",
    }

    def __init__(self_, matches: List[ActionMatch], request_id: str, total_matches: int, **kwargs):
        """


        :param matches: The matching actions.
        :type matches: [ActionMatch]

        :param request_id: The request ID.
        :type request_id: str

        :param total_matches: The total number of matches.
        :type total_matches: int
        """
        super().__init__(kwargs)

        self_.matches = matches
        self_.request_id = request_id
        self_.total_matches = total_matches
