# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CommitmentsUnit(ModelNormal):
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

    def __init__(self_, family: str, id: int, name: str, plural: str, scale_factor: float, short_name: str, **kwargs):
        """
        Unit metadata for a numeric metric.

        :param family: The unit family (for example, percentage or money).
        :type family: str

        :param id: The unit identifier.
        :type id: int

        :param name: The unit name (for example, percent or dollar).
        :type name: str

        :param plural: The plural form of the unit name.
        :type plural: str

        :param scale_factor: The scale factor for the unit.
        :type scale_factor: float

        :param short_name: The abbreviated unit name (for example, % or $).
        :type short_name: str
        """
        super().__init__(kwargs)

        self_.family = family
        self_.id = id
        self_.name = name
        self_.plural = plural
        self_.scale_factor = scale_factor
        self_.short_name = short_name
