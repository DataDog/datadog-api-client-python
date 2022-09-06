# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CanceledDowntimesIds(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "cancelled_ids": ([int],),
        }

    attribute_map = {
        "cancelled_ids": "cancelled_ids",
    }

    def __init__(self_, *args, **kwargs):
        """
        Object containing array of IDs of canceled downtimes.

        :param cancelled_ids: ID of downtimes that were canceled.
        :type cancelled_ids: [int], optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
