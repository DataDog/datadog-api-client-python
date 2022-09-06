# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SearchSLOResponseDataAttributesFacetsObjectString(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "count": (int,),
            "name": (str,),
        }

    attribute_map = {
        "count": "count",
        "name": "name",
    }

    def __init__(self_, *args, **kwargs):
        """
        Facet

        :param count: Count
        :type count: int, optional

        :param name: Facet
        :type name: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
