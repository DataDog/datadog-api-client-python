# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageCustomReportsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "computed_on": (str,),
            "end_date": (str,),
            "size": (int,),
            "start_date": (str,),
            "tags": ([str],),
        }

    attribute_map = {
        "computed_on": "computed_on",
        "end_date": "end_date",
        "size": "size",
        "start_date": "start_date",
        "tags": "tags",
    }

    def __init__(self, *args, **kwargs):
        """
        The response containing attributes for custom reports.

        :param computed_on: The date the specified custom report was computed.
        :type computed_on: str, optional

        :param end_date: The ending date of custom report.
        :type end_date: str, optional

        :param size: size
        :type size: int, optional

        :param start_date: The starting date of custom report.
        :type start_date: str, optional

        :param tags: A list of tags to apply to custom reports.
        :type tags: [str], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageCustomReportsAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
