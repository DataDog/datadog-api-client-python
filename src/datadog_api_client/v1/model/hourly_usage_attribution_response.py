# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class HourlyUsageAttributionResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.hourly_usage_attribution_metadata import HourlyUsageAttributionMetadata
        from datadog_api_client.v1.model.hourly_usage_attribution_body import HourlyUsageAttributionBody

        return {
            "metadata": (HourlyUsageAttributionMetadata,),
            "usage": ([HourlyUsageAttributionBody],),
        }

    attribute_map = {
        "metadata": "metadata",
        "usage": "usage",
    }

    def __init__(self_, *args, **kwargs):
        """
        Response containing the hourly usage attribution by tag(s).

        :param metadata: The object containing document metadata.
        :type metadata: HourlyUsageAttributionMetadata, optional

        :param usage: Get the hourly usage attribution by tag(s).
        :type usage: [HourlyUsageAttributionBody], optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
