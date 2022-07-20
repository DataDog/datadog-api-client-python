# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricBulkTagConfigStatusAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_bulk_tag_config_email_list import MetricBulkTagConfigEmailList
        from datadog_api_client.v2.model.metric_bulk_tag_config_tag_name_list import MetricBulkTagConfigTagNameList

        return {
            "emails": (MetricBulkTagConfigEmailList,),
            "status": (str,),
            "tags": (MetricBulkTagConfigTagNameList,),
        }

    attribute_map = {
        "emails": "emails",
        "status": "status",
        "tags": "tags",
    }

    def __init__(self, *args, **kwargs):
        """
        Optional attributes for the status of a bulk tag configuration request.

        :param emails: A list of account emails to notify when the configuration is applied.
        :type emails: MetricBulkTagConfigEmailList, optional

        :param status: The status of the request.
        :type status: str, optional

        :param tags: A list of tag names to apply to the configuration.
        :type tags: MetricBulkTagConfigTagNameList, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricBulkTagConfigStatusAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
