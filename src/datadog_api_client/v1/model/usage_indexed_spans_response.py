# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageIndexedSpansResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.usage_indexed_spans_hour import UsageIndexedSpansHour

        return {
            "usage": ([UsageIndexedSpansHour],),
        }

    attribute_map = {
        "usage": "usage",
    }

    def __init__(self, *args, **kwargs):
        """
        A response containing indexed spans usage.

        :param usage: Array with the number of hourly traces indexed for a given organization.
        :type usage: [UsageIndexedSpansHour], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageIndexedSpansResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
