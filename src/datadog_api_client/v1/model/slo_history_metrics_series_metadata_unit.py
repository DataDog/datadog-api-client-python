# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class SLOHistoryMetricsSeriesMetadataUnit(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "family": (str,),
            "id": (int,),
            "name": (str,),
            "plural": (str, none_type),
            "scale_factor": (float,),
            "short_name": (str, none_type),
        }

    attribute_map = {
        "family": "family",
        "id": "id",
        "name": "name",
        "plural": "plural",
        "scale_factor": "scale_factor",
        "short_name": "short_name",
    }

    def __init__(self, *args, **kwargs):
        """
        An Object of metric units.

        :param family: The family of metric unit, for example ``bytes`` is the family for ``kibibyte`` , ``byte`` , and ``bit`` units.
        :type family: str, optional

        :param id: The ID of the metric unit.
        :type id: int, optional

        :param name: The unit of the metric, for instance ``byte``.
        :type name: str, optional

        :param plural: The plural Unit of metric, for instance ``bytes``.
        :type plural: str, none_type, optional

        :param scale_factor: The scale factor of metric unit, for instance ``1.0``.
        :type scale_factor: float, optional

        :param short_name: A shorter and abbreviated version of the metric unit, for instance ``B``.
        :type short_name: str, none_type, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLOHistoryMetricsSeriesMetadataUnit, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
