# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CommitmentsQueryDefinitionFormula(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "formula": (str,),
            "id": (str,),
        }

    attribute_map = {
        "formula": "formula",
        "id": "id",
    }

    def __init__(self_, formula: str, id: str, **kwargs):
        """
        A formula of a query definition.

        :param formula: The formula expression over the named queries.
        :type formula: str

        :param id: The name of the response value the formula produces.
        :type id: str
        """
        super().__init__(kwargs)

        self_.formula = formula
        self_.id = id
