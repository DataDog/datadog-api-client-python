# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonthlyUsageAttributionResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monthly_usage_attribution_metadata import MonthlyUsageAttributionMetadata
        from datadog_api_client.v1.model.monthly_usage_attribution_body import MonthlyUsageAttributionBody

        return {
            "metadata": (MonthlyUsageAttributionMetadata,),
            "usage": ([MonthlyUsageAttributionBody],),
        }

    attribute_map = {
        "metadata": "metadata",
        "usage": "usage",
    }

    def __init__(self_, *args, **kwargs):
        """
        Response containing the monthly Usage Summary by tag(s).

        :param metadata: The object containing document metadata.
        :type metadata: MonthlyUsageAttributionMetadata, optional

        :param usage: Get usage summary by tag(s).
        :type usage: [MonthlyUsageAttributionBody], optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
