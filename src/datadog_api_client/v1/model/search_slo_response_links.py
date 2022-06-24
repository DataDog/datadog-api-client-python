# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SearchSLOResponseLinks(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "first": (str,),
            "last": (str,),
            "next": (str,),
            "prev": (str,),
            "self": (str,),
        }

    attribute_map = {
        "first": "first",
        "last": "last",
        "next": "next",
        "prev": "prev",
        "self": "self",
    }

    def __init__(self, *args, **kwargs):
        """
        Pagination links.

        :param first: Link to last page.
        :type first: str, optional

        :param last: Link to first page.
        :type last: str, optional

        :param next: Link to the next page.
        :type next: str, optional

        :param prev: Link to previous page.
        :type prev: str, optional

        :param self: Link to current page.
        :type self: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SearchSLOResponseLinks, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
