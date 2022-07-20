# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricDistinctVolume(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_distinct_volume_attributes import MetricDistinctVolumeAttributes
        from datadog_api_client.v2.model.metric_distinct_volume_type import MetricDistinctVolumeType

        return {
            "attributes": (MetricDistinctVolumeAttributes,),
            "id": (str,),
            "type": (MetricDistinctVolumeType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        Object for a single metric's distinct volume.

        :param attributes: Object containing the definition of a metric's distinct volume.
        :type attributes: MetricDistinctVolumeAttributes, optional

        :param id: The metric name for this resource.
        :type id: str, optional

        :param type: The metric distinct volume type.
        :type type: MetricDistinctVolumeType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricDistinctVolume, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
