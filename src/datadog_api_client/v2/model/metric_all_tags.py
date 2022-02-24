# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.metric_all_tags_attributes import MetricAllTagsAttributes
    from datadog_api_client.v2.model.metric_type import MetricType

    globals()["MetricAllTagsAttributes"] = MetricAllTagsAttributes
    globals()["MetricType"] = MetricType


class MetricAllTags(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "attributes": (MetricAllTagsAttributes,),
            "id": (str,),
            "type": (MetricType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Object for a single metric's indexed tags.

        :param attributes: Object containing the definition of a metric's tags.
        :type attributes: MetricAllTagsAttributes, optional

        :param id: The metric name for this resource.
        :type id: str, optional

        :param type: The metric resource type.
        :type type: MetricType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricAllTags, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
