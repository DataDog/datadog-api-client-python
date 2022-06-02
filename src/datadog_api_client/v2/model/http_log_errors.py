# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class HTTPLogErrors(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.http_log_error import HTTPLogError

        return {
            "errors": ([HTTPLogError],),
        }

    attribute_map = {
        "errors": "errors",
    }

    def __init__(self, *args, **kwargs):
        """
        Invalid query performed.

        :param errors: Structured errors.
        :type errors: [HTTPLogError], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(HTTPLogErrors, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
