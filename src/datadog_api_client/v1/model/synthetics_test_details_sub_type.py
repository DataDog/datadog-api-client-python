# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ApiTypeError,
    ModelSimple,
    cached_property,
)


class SyntheticsTestDetailsSubType(ModelSimple):

    allowed_values = {
        "value": {
            "HTTP": "http",
            "SSL": "ssl",
            "TCP": "tcp",
            "DNS": "dns",
            "MULTI": "multi",
            "ICMP": "icmp",
            "UDP": "udp",
            "WEBSOCKET": "websocket",
            "GRPC": "grpc",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }

    def __init__(self, *args, **kwargs):
        """
        The subtype of the Synthetic API test, `http`, `ssl`, `tcp`,
        `dns`, `icmp`, `udp`, `websocket`, `grpc` or `multi`.

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: Must be one of ["http", "ssl", "tcp", "dns", "multi", "icmp", "udp", "websocket", "grpc"].
        :type value: str
        """
        super().__init__(kwargs)

        if "value" in kwargs:
            value = kwargs.pop("value")
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=self._path_to_item,
                valid_classes=(self.__class__,),
            )

        self._check_pos_args(args)

        self.value = value

        self._check_kw_args(kwargs)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""
        return cls(*args, **kwargs)
