# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


class DemSearchInferredJourneysResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "data": ([bool, date, datetime, dict, float, int, list, str, UUID, none_type],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[Any], **kwargs):
        """
        Response body for searching inferred journeys. Contains either candidate or ignored items depending on the ``status`` query parameter.

        :param data: List of inferred journey items matching the search criteria.
        :type data: [bool, date, datetime, dict, float, int, list, str, UUID, none_type]
        """
        super().__init__(kwargs)

        self_.data = data
