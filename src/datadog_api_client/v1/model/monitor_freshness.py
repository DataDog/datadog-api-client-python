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


class MonitorFreshness(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "error": (str, none_type),
            "is_fresh": (bool,),
            "last_evaluated": (datetime,),
        }

    attribute_map = {
        "error": "error",
        "is_fresh": "is_fresh",
        "last_evaluated": "last_evaluated",
    }

    def __init__(
        self_,
        error: Union[str, none_type, UnsetType] = unset,
        is_fresh: Union[bool, UnsetType] = unset,
        last_evaluated: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        The freshness of the monitor, indicating if the monitor evaluation is up to date. **This feature is currently in private beta.**

        :param error: The error message if the monitor freshness was not able to be determined.
        :type error: str, none_type, optional

        :param is_fresh: Whether the monitor evaluation is up to date.
        :type is_fresh: bool, optional

        :param last_evaluated: The timestamp of the last evaluation.
        :type last_evaluated: datetime, optional
        """
        if error is not unset:
            kwargs["error"] = error
        if is_fresh is not unset:
            kwargs["is_fresh"] = is_fresh
        if last_evaluated is not unset:
            kwargs["last_evaluated"] = last_evaluated
        super().__init__(kwargs)
