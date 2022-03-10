# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AuditLogsQueryPageOptions(ModelNormal):
    validations = {
        "limit": {
            "inclusive_maximum": 1000,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "cursor": (str,),
            "limit": (int,),
        }

    attribute_map = {
        "cursor": "cursor",
        "limit": "limit",
    }

    def __init__(self, *args, **kwargs):
        """
        Paging attributes for listing events.

        :param cursor: List following results with a cursor provided in the previous query.
        :type cursor: str, optional

        :param limit: Maximum number of events in the response.
        :type limit: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AuditLogsQueryPageOptions, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
