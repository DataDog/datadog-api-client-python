# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DemTestSuiteNested(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "name": (str,),
        }

    attribute_map = {
        "id": "id",
        "name": "name",
    }

    def __init__(self_, id: str, name: str, **kwargs):
        """
        A test suite associated with a DEM resource.

        :param id: The ID of the test suite.
        :type id: str

        :param name: The name of the test suite.
        :type name: str
        """
        super().__init__(kwargs)

        self_.id = id
        self_.name = name
