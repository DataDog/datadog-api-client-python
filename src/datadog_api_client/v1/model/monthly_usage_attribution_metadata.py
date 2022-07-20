# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonthlyUsageAttributionMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.usage_attribution_aggregates import UsageAttributionAggregates
        from datadog_api_client.v1.model.monthly_usage_attribution_pagination import MonthlyUsageAttributionPagination

        return {
            "aggregates": (UsageAttributionAggregates,),
            "pagination": (MonthlyUsageAttributionPagination,),
        }

    attribute_map = {
        "aggregates": "aggregates",
        "pagination": "pagination",
    }

    def __init__(self, *args, **kwargs):
        """
        The object containing document metadata.

        :param aggregates: An array of available aggregates.
        :type aggregates: UsageAttributionAggregates, optional

        :param pagination: The metadata for the current pagination.
        :type pagination: MonthlyUsageAttributionPagination, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MonthlyUsageAttributionMetadata, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
