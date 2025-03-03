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


class DataTransformProperties(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "outputs": (str,),
        }

    attribute_map = {
        "outputs": "outputs",
    }

    def __init__(self_, outputs: Union[str, UnsetType] = unset, **kwargs):
        """
        The properties of the data transformer.

        :param outputs: A JavaScript function that returns the transformed data.
        :type outputs: str, optional
        """
        if outputs is not unset:
            kwargs["outputs"] = outputs
        super().__init__(kwargs)
