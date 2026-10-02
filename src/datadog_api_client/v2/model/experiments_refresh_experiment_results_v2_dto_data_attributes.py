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


class ExperimentsRefreshExperimentResultsV2DTODataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "success": (bool,),
        }

    attribute_map = {
        "success": "success",
    }

    def __init__(self_, success: Union[bool, UnsetType] = unset, **kwargs):
        """
        Details of the experiment refresh result.

        :param success: Whether the refresh request succeeded.
        :type success: bool, optional
        """
        if success is not unset:
            kwargs["success"] = success
        super().__init__(kwargs)
