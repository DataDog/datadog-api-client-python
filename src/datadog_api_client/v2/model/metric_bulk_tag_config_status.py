# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.metric_bulk_tag_config_status_attributes import MetricBulkTagConfigStatusAttributes
    from datadog_api_client.v2.model.metric_bulk_configure_tags_type import MetricBulkConfigureTagsType

    globals()["MetricBulkTagConfigStatusAttributes"] = MetricBulkTagConfigStatusAttributes
    globals()["MetricBulkConfigureTagsType"] = MetricBulkConfigureTagsType


class MetricBulkTagConfigStatus(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "attributes": (MetricBulkTagConfigStatusAttributes,),
            "id": (str,),
            "type": (MetricBulkConfigureTagsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, id, type, *args, **kwargs):
        """
        The status of a request to bulk configure metric tags.
        It contains the fields from the original request for reference.

        :param attributes: Optional attributes for the status of a bulk tag configuration request.
        :type attributes: MetricBulkTagConfigStatusAttributes, optional

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

        self = super(MetricBulkTagConfigStatus, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type
        return self
