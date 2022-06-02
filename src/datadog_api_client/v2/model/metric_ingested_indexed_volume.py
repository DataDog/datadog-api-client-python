# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricIngestedIndexedVolume(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_ingested_indexed_volume_attributes import (
            MetricIngestedIndexedVolumeAttributes,
        )
        from datadog_api_client.v2.model.metric_ingested_indexed_volume_type import MetricIngestedIndexedVolumeType

        return {
            "attributes": (MetricIngestedIndexedVolumeAttributes,),
            "id": (str,),
            "type": (MetricIngestedIndexedVolumeType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        Object for a single metric's ingested and indexed volume.

        :param attributes: Object containing the definition of a metric's ingested and indexed volume.
        :type attributes: MetricIngestedIndexedVolumeAttributes, optional

        :param id: The metric name for this resource.
        :type id: str, optional

        :param type: The metric ingested and indexed volume type.
        :type type: MetricIngestedIndexedVolumeType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricIngestedIndexedVolume, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
