# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SLOListResponseMetadataPage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "total_count": (int,),
            "total_filtered_count": (int,),
        }

    attribute_map = {
        "total_count": "total_count",
        "total_filtered_count": "total_filtered_count",
    }

    def __init__(self, *args, **kwargs):
        """
        The object containing information about the pages of the list of SLOs.

        :param total_count: The total number of resources that could be retrieved ignoring the parameters and filters in the request.
        :type total_count: int, optional

        :param total_filtered_count: The total number of resources that match the parameters and filters in the request. This attribute can be used by a client to determine the total number of pages.
        :type total_filtered_count: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLOListResponseMetadataPage, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
