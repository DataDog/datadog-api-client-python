# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "integration": (str,),
            "per_unit": (str,),
            "short_name": (str,),
            "statsd_interval": (int,),
            "type": (str,),
            "unit": (str,),
        }

    attribute_map = {
        "description": "description",
        "integration": "integration",
        "per_unit": "per_unit",
        "short_name": "short_name",
        "statsd_interval": "statsd_interval",
        "type": "type",
        "unit": "unit",
    }
    read_only_vars = {
        "integration",
    }

    def __init__(self, *args, **kwargs):
        """
        Object with all metric related metadata.

        :param description: Metric description.
        :type description: str, optional

        :param integration: Name of the integration that sent the metric if applicable.
        :type integration: str, optional

        :param per_unit: Per unit of the metric such as ``second`` in ``bytes per second``.
        :type per_unit: str, optional

        :param short_name: A more human-readable and abbreviated version of the metric name.
        :type short_name: str, optional

        :param statsd_interval: StatsD flush interval of the metric in seconds if applicable.
        :type statsd_interval: int, optional

        :param type: Metric type such as ``gauge`` or ``rate``.
        :type type: str, optional

        :param unit: Primary unit of the metric such as ``byte`` or ``operation``.
        :type unit: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricMetadata, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
