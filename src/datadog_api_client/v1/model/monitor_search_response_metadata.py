# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonitorSearchResponseMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "page": (int,),
            "page_count": (int,),
            "per_page": (int,),
            "total_count": (int,),
        }

    attribute_map = {
        "page": "page",
        "page_count": "page_count",
        "per_page": "per_page",
        "total_count": "total_count",
    }
    read_only_vars = {
        "page",
        "page_count",
        "per_page",
        "total_count",
    }

    def __init__(self, *args, **kwargs):
        """
        Metadata about the response.

        :param page: The page to start paginating from.
        :type page: int, optional

        :param page_count: The number of pages.
        :type page_count: int, optional

        :param per_page: The number of monitors to return per page.
        :type per_page: int, optional

        :param total_count: The total number of monitors.
        :type total_count: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MonitorSearchResponseMetadata, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
