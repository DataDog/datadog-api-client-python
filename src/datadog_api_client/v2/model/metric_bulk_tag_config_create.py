# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.metric_bulk_tag_config_create_attributes import MetricBulkTagConfigCreateAttributes
    from datadog_api_client.v2.model.metric_bulk_configure_tags_type import MetricBulkConfigureTagsType

    globals()["MetricBulkTagConfigCreateAttributes"] = MetricBulkTagConfigCreateAttributes
    globals()["MetricBulkConfigureTagsType"] = MetricBulkConfigureTagsType


class MetricBulkTagConfigCreate(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "attributes": (MetricBulkTagConfigCreateAttributes,),
            "id": (str,),
            "type": (MetricBulkConfigureTagsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self, id, type, *args, **kwargs):
        """
        Request object to bulk configure tags for metrics matching the given prefix.

        :param attributes: Optional parameters for bulk creating metric tag configurations.
        :type attributes: MetricBulkTagConfigCreateAttributes, optional

        :param id: A text prefix to match against metric names.
        :type id: str

        :param type: The metric bulk configure tags resource.
        :type type: MetricBulkConfigureTagsType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type

    @classmethod
    def _from_openapi_data(cls, id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricBulkTagConfigCreate, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type
        return self
