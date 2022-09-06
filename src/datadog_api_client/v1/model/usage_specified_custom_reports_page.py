# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageSpecifiedCustomReportsPage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "total_count": (int,),
        }

    attribute_map = {
        "total_count": "total_count",
    }

    def __init__(self_, *args, **kwargs):
        """
        The object containing page total count for specified ID.

        :param total_count: Total page count.
        :type total_count: int, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
