# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class ErrorErrorsItemsLinks(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "about": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "type": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
        }

    attribute_map = {
        "about": "about",
        "type": "type",
    }

    def __init__(self_, about: Union[Any, UnsetType] = unset, type: Union[Any, UnsetType] = unset, **kwargs):
        """
        The definition of ``ErrorErrorsItemsLinks`` object.

        :param about: The ``links`` ``about``.
        :type about: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional

        :param type: The ``links`` ``type``.
        :type type: bool, date, datetime, dict, float, int, list, str, UUID, none_type, optional
        """
        if about is not unset:
            kwargs["about"] = about
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
