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


class BudgetAttributesCostsUnit(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "family": (str,),
            "id": (str,),
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
        id: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        plural: Union[str, UnsetType] = unset,
        scale_factor: Union[float, UnsetType] = unset,
        short_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The unit used for all cost values in the response.

        :param family: The unit family (for example, ``currency`` ).
        :type family: str, optional

        :param id: The unique identifier for the unit.
        :type id: str, optional

        :param name: The full name of the unit.
        :type name: str, optional

        :param plural: The plural form of the unit name.
        :type plural: str, optional

        :param scale_factor: The scale factor applied to raw cost values.
        :type scale_factor: float, optional

        :param short_name: The abbreviated unit name.
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
