# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LogsIndexListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.logs_index import LogsIndex

        return {
            "indexes": ([LogsIndex],),
        }

    attribute_map = {
        "indexes": "indexes",
    }

    def __init__(self, *args, **kwargs):
        """
        Object with all Index configurations for a given organization.

        :param indexes: Array of Log index configurations.
        :type indexes: [LogsIndex], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsIndexListResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
