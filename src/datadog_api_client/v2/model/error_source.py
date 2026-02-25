# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class ErrorSource(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "header": (str, none_type),
            "parameter": (str, none_type),
            "pointer": (str, none_type),
        }

    attribute_map = {
        "header": "header",
        "parameter": "parameter",
        "pointer": "pointer",
    }

    def __init__(
        self_,
        header: Union[str, none_type, UnsetType] = unset,
        parameter: Union[str, none_type, UnsetType] = unset,
        pointer: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        An object containing references to the primary source of the error.
        See: https://jsonapi.org/format/#error-objects

        :param header:
        :type header: str, none_type, optional

        :param parameter:
        :type parameter: str, none_type, optional

        :param pointer:
        :type pointer: str, none_type, optional
        """
        if header is not unset:
            kwargs["header"] = header
        if parameter is not unset:
            kwargs["parameter"] = parameter
        if pointer is not unset:
            kwargs["pointer"] = pointer
        super().__init__(kwargs)
