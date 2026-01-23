# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CustomRuleRevisionTest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "annotation_count": (int,),
            "code": (str,),
            "filename": (str,),
        }

    attribute_map = {
        "annotation_count": "annotation_count",
        "code": "code",
        "filename": "filename",
    }

    def __init__(self_, annotation_count: int, code: str, filename: str, **kwargs):
        """


        :param annotation_count: Expected violation count
        :type annotation_count: int

        :param code: Test code
        :type code: str

        :param filename: Test filename
        :type filename: str
        """
        super().__init__(kwargs)

        self_.annotation_count = annotation_count
        self_.code = code
        self_.filename = filename
