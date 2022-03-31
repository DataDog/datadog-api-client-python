# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.usage_custom_reports_data import UsageCustomReportsData
    from datadog_api_client.v1.model.usage_custom_reports_meta import UsageCustomReportsMeta

    globals()["UsageCustomReportsData"] = UsageCustomReportsData
    globals()["UsageCustomReportsMeta"] = UsageCustomReportsMeta


class UsageCustomReportsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "data": ([UsageCustomReportsData],),
            "meta": (UsageCustomReportsMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self, *args, **kwargs):
        """
        Response containing available custom reports.

        :param data: An array of available custom reports.
        :type data: [UsageCustomReportsData], optional

        :param meta: The object containing document metadata.
        :type meta: UsageCustomReportsMeta, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageCustomReportsResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
