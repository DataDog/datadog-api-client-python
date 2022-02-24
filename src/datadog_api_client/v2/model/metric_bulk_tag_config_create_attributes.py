# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.metric_bulk_tag_config_email_list import MetricBulkTagConfigEmailList
    from datadog_api_client.v2.model.metric_bulk_tag_config_tag_name_list import MetricBulkTagConfigTagNameList

    globals()["MetricBulkTagConfigEmailList"] = MetricBulkTagConfigEmailList
    globals()["MetricBulkTagConfigTagNameList"] = MetricBulkTagConfigTagNameList


class MetricBulkTagConfigCreateAttributes(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "emails": (MetricBulkTagConfigEmailList,),
            "tags": (MetricBulkTagConfigTagNameList,),
        }

    attribute_map = {
        "emails": "emails",
        "tags": "tags",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Optional parameters for bulk creating metric tag configurations.

        :param emails: A list of account emails to notify when the configuration is applied.
        :type emails: MetricBulkTagConfigEmailList, optional

        :param tags: A list of tag names to apply to the configuration.
        :type tags: MetricBulkTagConfigTagNameList, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricBulkTagConfigCreateAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
