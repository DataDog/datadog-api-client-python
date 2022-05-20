# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.metric_estimate_attributes import MetricEstimateAttributes
    from datadog_api_client.v2.model.metric_estimate_resource_type import MetricEstimateResourceType

    globals()["MetricEstimateAttributes"] = MetricEstimateAttributes
    globals()["MetricEstimateResourceType"] = MetricEstimateResourceType


class MetricEstimate(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "attributes": (MetricEstimateAttributes,),
            "id": (str,),
            "type": (MetricEstimateResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        Object for a metric cardinality estimate.

        :param attributes: Object containing the definition of a metric estimate attribute.
        :type attributes: MetricEstimateAttributes, optional

        :param id: The metric name for this resource.
        :type id: str, optional

        :param type: The metric estimate resource type.
        :type type: MetricEstimateResourceType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricEstimate, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
