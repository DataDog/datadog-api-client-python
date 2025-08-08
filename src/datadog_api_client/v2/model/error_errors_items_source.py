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


class ErrorErrorsItemsSource(ModelNormal):
    _nullable = True

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
        The definition of ``ErrorErrorsItemsSource`` object.

        :param header: The ``source`` ``header``.
        :type header: str, optional

        :param parameter: The ``source`` ``parameter``.
        :type parameter: str, optional

        :param pointer: The ``source`` ``pointer``.
        :type pointer: str, optional
        """
        if header is not unset:
            kwargs["header"] = header
        if parameter is not unset:
            kwargs["parameter"] = parameter
        if pointer is not unset:
            kwargs["pointer"] = pointer
        super().__init__(kwargs)
