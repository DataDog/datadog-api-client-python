# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityFilterAttributes(ModelNormal):
    validations = {
        "version": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_filter_exclusion_filter_response import (
            SecurityFilterExclusionFilterResponse,
        )
        from datadog_api_client.v2.model.security_filter_filtered_data_type import SecurityFilterFilteredDataType

        return {
            "exclusion_filters": ([SecurityFilterExclusionFilterResponse],),
            "filtered_data_type": (SecurityFilterFilteredDataType,),
            "is_builtin": (bool,),
            "is_enabled": (bool,),
            "name": (str,),
            "query": (str,),
            "version": (int,),
        }

    attribute_map = {
        "exclusion_filters": "exclusion_filters",
        "filtered_data_type": "filtered_data_type",
        "is_builtin": "is_builtin",
        "is_enabled": "is_enabled",
        "name": "name",
        "query": "query",
        "version": "version",
    }

    def __init__(self, *args, **kwargs):
        """
        The object describing a security filter.

        :param exclusion_filters: The list of exclusion filters applied in this security filter.
        :type exclusion_filters: [SecurityFilterExclusionFilterResponse], optional

        :param filtered_data_type: The filtered data type.
        :type filtered_data_type: SecurityFilterFilteredDataType, optional

        :param is_builtin: Whether the security filter is the built-in filter.
        :type is_builtin: bool, optional

        :param is_enabled: Whether the security filter is enabled.
        :type is_enabled: bool, optional

        :param name: The security filter name.
        :type name: str, optional

        :param query: The security filter query. Logs accepted by this query will be accepted by this filter.
        :type query: str, optional

        :param version: The version of the security filter.
        :type version: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityFilterAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
