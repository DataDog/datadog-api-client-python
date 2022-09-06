# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageOnlineArchiveResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.usage_online_archive_hour import UsageOnlineArchiveHour

        return {
            "usage": ([UsageOnlineArchiveHour],),
        }

    attribute_map = {
        "usage": "usage",
    }

    def __init__(self_, *args, **kwargs):
        """
        Online Archive usage response.

        :param usage: Response containing Online Archive usage.
        :type usage: [UsageOnlineArchiveHour], optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
