# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageSpecifiedCustomReportsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.usage_specified_custom_reports_data import UsageSpecifiedCustomReportsData
        from datadog_api_client.v1.model.usage_specified_custom_reports_meta import UsageSpecifiedCustomReportsMeta

        return {
            "data": (UsageSpecifiedCustomReportsData,),
            "meta": (UsageSpecifiedCustomReportsMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self, *args, **kwargs):
        """
        Returns available specified custom reports.

        :param data: Response containing date and type for specified custom reports.
        :type data: UsageSpecifiedCustomReportsData, optional

        :param meta: The object containing document metadata.
        :type meta: UsageSpecifiedCustomReportsMeta, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageSpecifiedCustomReportsResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
