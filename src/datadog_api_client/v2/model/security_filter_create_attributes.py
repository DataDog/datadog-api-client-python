# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityFilterCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_filter_exclusion_filter import SecurityFilterExclusionFilter
        from datadog_api_client.v2.model.security_filter_filtered_data_type import SecurityFilterFilteredDataType

        return {
            "exclusion_filters": ([SecurityFilterExclusionFilter],),
            "filtered_data_type": (SecurityFilterFilteredDataType,),
            "is_enabled": (bool,),
            "name": (str,),
            "query": (str,),
        }

    attribute_map = {
        "exclusion_filters": "exclusion_filters",
        "filtered_data_type": "filtered_data_type",
        "is_enabled": "is_enabled",
        "name": "name",
        "query": "query",
    }

    def __init__(self, exclusion_filters, filtered_data_type, is_enabled, name, query, *args, **kwargs):
        """
        Object containing the attributes of the security filter to be created.

        :param exclusion_filters: Exclusion filters to exclude some logs from the security filter.
        :type exclusion_filters: [SecurityFilterExclusionFilter]

        :param filtered_data_type: The filtered data type.
        :type filtered_data_type: SecurityFilterFilteredDataType

        :param is_enabled: Whether the security filter is enabled.
        :type is_enabled: bool

        :param name: The name of the security filter.
        :type name: str

        :param query: The query of the security filter.
        :type query: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.exclusion_filters = exclusion_filters
        self.filtered_data_type = filtered_data_type
        self.is_enabled = is_enabled
        self.name = name
        self.query = query

    @classmethod
    def _from_openapi_data(cls, exclusion_filters, filtered_data_type, is_enabled, name, query, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityFilterCreateAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.exclusion_filters = exclusion_filters
        self.filtered_data_type = filtered_data_type
        self.is_enabled = is_enabled
        self.name = name
        self.query = query
        return self
