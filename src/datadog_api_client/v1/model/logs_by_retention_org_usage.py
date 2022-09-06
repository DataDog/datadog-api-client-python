# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsByRetentionOrgUsage(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_retention_sum_usage import LogsRetentionSumUsage

        return {
            "usage": ([LogsRetentionSumUsage],),
        }

    attribute_map = {
        "usage": "usage",
    }

    def __init__(self_, *args, **kwargs):
        """
        Indexed logs usage by retention for a single organization.

        :param usage: Indexed logs usage for each active retention for the organization.
        :type usage: [LogsRetentionSumUsage], optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
