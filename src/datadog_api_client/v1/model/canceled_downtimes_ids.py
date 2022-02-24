# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class CanceledDowntimesIds(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "cancelled_ids": ([int],),
        }

    attribute_map = {
        "cancelled_ids": "cancelled_ids",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Object containing array of IDs of canceled downtimes.

        :param cancelled_ids: ID of downtimes that were canceled.
        :type cancelled_ids: [int], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(CanceledDowntimesIds, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
