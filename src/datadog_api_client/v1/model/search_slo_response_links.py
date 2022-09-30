# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class SearchSLOResponseLinks(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "first": (str,),
            "last": (str, none_type),
            "next": (str,),
            "prev": (str, none_type),
            "self": (str,),
        }

    attribute_map = {
        "first": "first",
        "last": "last",
        "next": "next",
        "prev": "prev",
        "self": "self",
    }

    def __init__(self_, *args, **kwargs):
        """
        Pagination links.

        :param first: Link to last page.
        :type first: str, optional

        :param last: Link to first page.
        :type last: str, none_type, optional

        :param next: Link to the next page.
        :type next: str, optional

        :param prev: Link to previous page.
        :type prev: str, none_type, optional

        :param self: Link to current page.
        :type self: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
