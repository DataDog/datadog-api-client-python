# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class HourlyUsageResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.hourly_usage import HourlyUsage
        from datadog_api_client.v2.model.hourly_usage_metadata import HourlyUsageMetadata

        return {
            "data": ([HourlyUsage],),
            "meta": (HourlyUsageMetadata,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self, *args, **kwargs):
        """
        Hourly usage response.

        :param data: Response containing hourly usage.
        :type data: [HourlyUsage], optional

        :param meta: The object containing document metadata.
        :type meta: HourlyUsageMetadata, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(HourlyUsageResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
