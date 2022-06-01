# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricBulkTagConfigDeleteAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_bulk_tag_config_email_list import MetricBulkTagConfigEmailList

        return {
            "emails": (MetricBulkTagConfigEmailList,),
        }

    attribute_map = {
        "emails": "emails",
    }

    def __init__(self, *args, **kwargs):
        """
        Optional parameters for bulk deleting metric tag configurations.

        :param emails: A list of account emails to notify when the configuration is applied.
        :type emails: MetricBulkTagConfigEmailList, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricBulkTagConfigDeleteAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
