# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class NotebooksResponsePage(ModelNormal):
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
        Pagination metadata returned by the API.

        :param total_count: The total number of notebooks that would be returned if the request was not filtered by `start` and `count` parameters.
        :type total_count: int, optional

        :param total_filtered_count: The total number of notebooks returned.
        :type total_filtered_count: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebooksResponsePage, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
