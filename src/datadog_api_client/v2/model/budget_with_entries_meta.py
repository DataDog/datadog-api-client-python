# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class BudgetWithEntriesMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "error": (str,),
        }

    attribute_map = {
        "error": "error",
    }

    def __init__(self_, error: str, **kwargs):
        """
        Additional information about errors encountered while retrieving budget cost data.

        :param error: A user-facing explanation of why budget cost data could not be retrieved.
        :type error: str
        """
        super().__init__(kwargs)

        self_.error = error
