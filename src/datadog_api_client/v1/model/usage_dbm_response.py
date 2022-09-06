# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageDBMResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.usage_dbm_hour import UsageDBMHour

        return {
            "usage": ([UsageDBMHour],),
        }

    attribute_map = {
        "usage": "usage",
    }

    def __init__(self_, *args, **kwargs):
        """
        Response containing the Database Monitoring usage for each hour for a given organization.

        :param usage: Get hourly usage for Database Monitoring
        :type usage: [UsageDBMHour], optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
