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


class LLMObsExperimentationContentPreview(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "limit": (int,),
        }

    attribute_map = {
        "limit": "limit",
    }

    def __init__(self_, limit: Union[int, UnsetType] = unset, **kwargs):
        """
        Options to control content preview truncation.

        :param limit: Maximum number of characters to include in content previews.
        :type limit: int, optional
        """
        if limit is not unset:
            kwargs["limit"] = limit
        super().__init__(kwargs)
