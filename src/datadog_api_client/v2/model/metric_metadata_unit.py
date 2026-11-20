# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class MetricMetadataUnit(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "family": (str,),
            "name": (str,),
            "plural": (str,),
            "scale_factor": (float,),
            "short_name": (str, none_type),
        }

    attribute_map = {
        "family": "family",
        "name": "name",
        "plural": "plural",
        "scale_factor": "scale_factor",
        "short_name": "short_name",
    }

    def __init__(
        self_, family: str, name: str, plural: str, scale_factor: float, short_name: Union[str, none_type], **kwargs
    ):
        """
        A unit of measure from the Datadog unit catalog, or ``null`` when no unit is set.

        :param family: Unit family, such as ``bytes`` , ``time`` , or ``percentage``.
        :type family: str

        :param name: Full name of the unit, such as ``byte``.
        :type name: str

        :param plural: Plural form of the unit name.
        :type plural: str

        :param scale_factor: Factor that converts a value in this unit to the base unit of its family.
        :type scale_factor: float

        :param short_name: Abbreviated unit name, or ``null`` if the unit has none.
        :type short_name: str, none_type
        """
        super().__init__(kwargs)

        self_.family = family
        self_.name = name
        self_.plural = plural
        self_.scale_factor = scale_factor
        self_.short_name = short_name
