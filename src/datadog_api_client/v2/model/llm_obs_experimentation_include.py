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


class LLMObsExperimentationInclude(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "user_data": (bool,),
        }

    attribute_map = {
        "user_data": "user_data",
    }

    def __init__(self_, user_data: Union[bool, UnsetType] = unset, **kwargs):
        """
        Additional data to include in the response.

        :param user_data: When ``true`` , enrich results with author user data (name and email).
        :type user_data: bool, optional
        """
        if user_data is not unset:
            kwargs["user_data"] = user_data
        super().__init__(kwargs)
