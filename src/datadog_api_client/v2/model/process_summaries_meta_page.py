# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ProcessSummariesMetaPage(ModelNormal):
    validations = {
        "size": {
            "inclusive_maximum": 10000,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "after": (str,),
            "size": (int,),
        }

    attribute_map = {
        "after": "after",
        "size": "size",
    }

    def __init__(self, *args, **kwargs):
        """
        Paging attributes.

        :param after: The cursor used to get the next results, if any. To make the next request, use the same
            parameters with the addition of the ``page[cursor]``.
        :type after: str, optional

        :param size: Number of results returned.
        :type size: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ProcessSummariesMetaPage, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
