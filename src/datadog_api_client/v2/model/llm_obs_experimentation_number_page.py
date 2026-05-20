# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class LLMObsExperimentationNumberPage(ModelNormal):
    validations = {
        "limit": {
            "inclusive_maximum": 2147483647,
        },
        "number": {
            "inclusive_maximum": 2147483647,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "limit": (int,),
            "number": (int,),
        }

    attribute_map = {
        "limit": "limit",
        "number": "number",
    }

    def __init__(self_, limit: Union[int, UnsetType] = unset, number: Union[int, UnsetType] = unset, **kwargs):
        """
        Offset-based pagination parameters for simple search.

        :param limit: Maximum number of results per page.
        :type limit: int, optional

        :param number: Page number to retrieve (1-indexed).
        :type number: int, optional
        """
        if limit is not unset:
            kwargs["limit"] = limit
        if number is not unset:
            kwargs["number"] = number
        super().__init__(kwargs)
