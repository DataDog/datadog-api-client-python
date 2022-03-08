# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class SecurityMonitoringSignalListRequestFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "_from": (datetime,),
            "query": (str,),
            "to": (datetime,),
        }

    attribute_map = {
        "_from": "from",
        "query": "query",
        "to": "to",
    }

    def __init__(self, *args, **kwargs):
        """
        Search filters for listing security signals.

        :param _from: The minimum timestamp for requested security signals.
        :type _from: datetime, optional

        :param query: Search query for listing security signals.
        :type query: str, optional

        :param to: The maximum timestamp for requested security signals.
        :type to: datetime, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityMonitoringSignalListRequestFilter, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
