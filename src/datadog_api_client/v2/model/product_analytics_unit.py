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


class ProductAnalyticsUnit(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "family": (str,),
            "id": (int,),
            "name": (str,),
            "plural": (str,),
            "scale_factor": (float,),
            "short_name": (str,),
        }

    attribute_map = {
        "family": "family",
        "id": "id",
        "name": "name",
        "plural": "plural",
        "scale_factor": "scale_factor",
        "short_name": "short_name",
    }

    def __init__(
        self_,
        family: Union[str, UnsetType] = unset,
        id: Union[int, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        plural: Union[str, UnsetType] = unset,
        scale_factor: Union[float, UnsetType] = unset,
        short_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A unit definition for metric values.

        :param family:
        :type family: str, optional

        :param id:
        :type id: int, optional

        :param name:
        :type name: str, optional

        :param plural:
        :type plural: str, optional

        :param scale_factor:
        :type scale_factor: float, optional

        :param short_name:
        :type short_name: str, optional
        """
        if family is not unset:
            kwargs["family"] = family
        if id is not unset:
            kwargs["id"] = id
        if name is not unset:
            kwargs["name"] = name
        if plural is not unset:
            kwargs["plural"] = plural
        if scale_factor is not unset:
            kwargs["scale_factor"] = scale_factor
        if short_name is not unset:
            kwargs["short_name"] = short_name
        super().__init__(kwargs)
