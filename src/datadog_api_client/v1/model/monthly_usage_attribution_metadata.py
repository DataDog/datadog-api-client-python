# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.monthly_usage_attribution_pagination import MonthlyUsageAttributionPagination
    from datadog_api_client.v1.model.usage_attribution_aggregates import UsageAttributionAggregates

    globals()["MonthlyUsageAttributionPagination"] = MonthlyUsageAttributionPagination
    globals()["UsageAttributionAggregates"] = UsageAttributionAggregates


class MonthlyUsageAttributionMetadata(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "aggregates": (UsageAttributionAggregates,),
            "pagination": (MonthlyUsageAttributionPagination,),
        }

    attribute_map = {
        "aggregates": "aggregates",
        "pagination": "pagination",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """MonthlyUsageAttributionMetadata - a model defined in OpenAPI

        Keyword Args:
            aggregates (UsageAttributionAggregates): [optional]
            pagination (MonthlyUsageAttributionPagination): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MonthlyUsageAttributionMetadata, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
