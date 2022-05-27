# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageSpecifiedCustomReportsMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.usage_specified_custom_reports_page import UsageSpecifiedCustomReportsPage

        return {
            "page": (UsageSpecifiedCustomReportsPage,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self, *args, **kwargs):
        """
        The object containing document metadata.

        :param page: The object containing page total count for specified ID.
        :type page: UsageSpecifiedCustomReportsPage, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageSpecifiedCustomReportsMeta, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
