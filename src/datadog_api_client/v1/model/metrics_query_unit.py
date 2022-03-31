# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricsQueryUnit(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "family": (str,),
            "name": (str,),
            "plural": (str,),
            "scale_factor": (float,),
            "short_name": (str,),
        }

    attribute_map = {
        "family": "family",
        "name": "name",
        "plural": "plural",
        "scale_factor": "scale_factor",
        "short_name": "short_name",
    }
    read_only_vars = {
        "family",
        "name",
        "plural",
        "scale_factor",
        "short_name",
    }

    def __init__(self, *args, **kwargs):
        """
        Object containing the metric unit family, scale factor, name, and short name.

        :param family: Unit family, allows for conversion between units of the same family, for scaling.
        :type family: str, optional

        :param name: Unit name
        :type name: str, optional

        :param plural: Plural form of the unit name.
        :type plural: str, optional

        :param scale_factor: Factor for scaling between units of the same family.
        :type scale_factor: float, optional

        :param short_name: Abbreviation of the unit.
        :type short_name: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricsQueryUnit, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
