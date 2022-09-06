# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageIngestedSpansResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.usage_ingested_spans_hour import UsageIngestedSpansHour

        return {
            "usage": ([UsageIngestedSpansHour],),
        }

    attribute_map = {
        "usage": "usage",
    }

    def __init__(self_, *args, **kwargs):
        """
        Response containing the ingested spans usage for each hour for a given organization.

        :param usage: Get hourly usage for ingested spans.
        :type usage: [UsageIngestedSpansHour], optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
