# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricSuggestedTagsAndAggregations(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_suggested_tags_attributes import MetricSuggestedTagsAttributes
        from datadog_api_client.v2.model.metric_active_configuration_type import MetricActiveConfigurationType

        return {
            "attributes": (MetricSuggestedTagsAttributes,),
            "id": (str,),
            "type": (MetricActiveConfigurationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        Object for a single metric's actively queried tags and aggregations.

        :param attributes: Object containing the definition of a metric's actively queried tags and aggregations.
        :type attributes: MetricSuggestedTagsAttributes, optional

        :param id: The metric name for this resource.
        :type id: str, optional

        :param type: The metric actively queried configuration resource type.
        :type type: MetricActiveConfigurationType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricSuggestedTagsAndAggregations, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
