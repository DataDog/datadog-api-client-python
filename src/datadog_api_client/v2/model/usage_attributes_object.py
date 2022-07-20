# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageAttributesObject(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.usage_time_series_object import UsageTimeSeriesObject
        from datadog_api_client.v2.model.hourly_usage_type import HourlyUsageType

        return {
            "org_name": (str,),
            "product_family": (str,),
            "public_id": (str,),
            "timeseries": ([UsageTimeSeriesObject],),
            "usage_type": (HourlyUsageType,),
        }

    attribute_map = {
        "org_name": "org_name",
        "product_family": "product_family",
        "public_id": "public_id",
        "timeseries": "timeseries",
        "usage_type": "usage_type",
    }

    def __init__(self, *args, **kwargs):
        """
        Usage attributes data.

        :param org_name: The organization name.
        :type org_name: str, optional

        :param product_family: The product for which usage is being reported.
        :type product_family: str, optional

        :param public_id: The organization public ID.
        :type public_id: str, optional

        :param timeseries: List of usage data reported for each requested hour.
        :type timeseries: [UsageTimeSeriesObject], optional

        :param usage_type: Usage type that is being measured.
        :type usage_type: HourlyUsageType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageAttributesObject, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
