# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MetricBulkTagConfigResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_bulk_tag_config_status import MetricBulkTagConfigStatus

        return {
            "data": (MetricBulkTagConfigStatus,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self, *args, **kwargs):
        """
        Wrapper for a single bulk tag configuration status response.

        :param data: The status of a request to bulk configure metric tags.
            It contains the fields from the original request for reference.
        :type data: MetricBulkTagConfigStatus, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricBulkTagConfigResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
