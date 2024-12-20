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


class JSONAPIErrorItemSource(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "header": (str,),
            "parameter": (str,),
            "pointer": (str,),
        }

    attribute_map = {
        "header": "header",
        "parameter": "parameter",
        "pointer": "pointer",
    }

    def __init__(
        self_,
        header: Union[str, UnsetType] = unset,
        parameter: Union[str, UnsetType] = unset,
        pointer: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        References to the source of the error.

        :param header: A string indicating the name of a single request header which caused the error.
        :type header: str, optional

        :param parameter: A string indicating which URI query parameter caused the error.
        :type parameter: str, optional

        :param pointer: A JSON pointer to the value in the request document that caused the error.
        :type pointer: str, optional
        """
        if header is not unset:
            kwargs["header"] = header
        if parameter is not unset:
            kwargs["parameter"] = parameter
        if pointer is not unset:
            kwargs["pointer"] = pointer
        super().__init__(kwargs)
