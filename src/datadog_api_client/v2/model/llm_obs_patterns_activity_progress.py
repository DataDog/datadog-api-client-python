# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


class LLMObsPatternsActivityProgress(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "started_at": (datetime, none_type),
            "status": (str,),
        }

    attribute_map = {
        "name": "name",
        "started_at": "started_at",
        "status": "status",
    }

    def __init__(self_, name: str, status: str, started_at: Union[datetime, none_type, UnsetType] = unset, **kwargs):
        """
        Progress information for a single step of a patterns run.

        :param name: Name of the step.
        :type name: str

        :param started_at: Timestamp when the step started. Null if the step has not started.
        :type started_at: datetime, none_type, optional

        :param status: Status of the step.
        :type status: str
        """
        if started_at is not unset:
            kwargs["started_at"] = started_at
        super().__init__(kwargs)

        self_.name = name
        self_.status = status
