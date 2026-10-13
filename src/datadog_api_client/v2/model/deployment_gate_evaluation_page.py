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


class DeploymentGateEvaluationPage(ModelNormal):
    validations = {
        "size": {
            "inclusive_maximum": 100,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "next_cursor": (str,),
            "size": (int,),
        }

    attribute_map = {
        "next_cursor": "next_cursor",
        "size": "size",
    }

    def __init__(self_, size: int, next_cursor: Union[str, UnsetType] = unset, **kwargs):
        """
        Cursor pagination information.

        :param next_cursor: Opaque cursor for the next page. Absent on the final page.
        :type next_cursor: str, optional

        :param size: Requested maximum number of resources in this page.
        :type size: int
        """
        if next_cursor is not unset:
            kwargs["next_cursor"] = next_cursor
        super().__init__(kwargs)

        self_.size = size
