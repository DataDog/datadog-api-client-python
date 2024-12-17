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


class AppBuilderErrorErrorsItemsSource(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "parameter": (str,),
            "pointer": (str,),
        }

    attribute_map = {
        "parameter": "parameter",
        "pointer": "pointer",
    }

    def __init__(self_, parameter: Union[str, UnsetType] = unset, pointer: Union[str, UnsetType] = unset, **kwargs):
        """
        The definition of ``AppBuilderErrorErrorsItemsSource`` object.

        :param parameter: The ``source`` ``parameter``.
        :type parameter: str, optional

        :param pointer: The ``source`` ``pointer``.
        :type pointer: str, optional
        """
        if parameter is not unset:
            kwargs["parameter"] = parameter
        if pointer is not unset:
            kwargs["pointer"] = pointer
        super().__init__(kwargs)
