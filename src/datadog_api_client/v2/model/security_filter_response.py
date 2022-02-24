# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.security_filter import SecurityFilter
    from datadog_api_client.v2.model.security_filter_meta import SecurityFilterMeta

    globals()["SecurityFilter"] = SecurityFilter
    globals()["SecurityFilterMeta"] = SecurityFilterMeta


class SecurityFilterResponse(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "data": (SecurityFilter,),
            "meta": (SecurityFilterMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Response object which includes a single security filter.

        :param data: The security filter's properties.
        :type data: SecurityFilter, optional

        :param meta: Optional metadata associated to the response.
        :type meta: SecurityFilterMeta, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityFilterResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
