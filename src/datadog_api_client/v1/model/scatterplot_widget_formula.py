# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ScatterplotWidgetFormula(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.scatterplot_dimension import ScatterplotDimension

        return {
            "alias": (str,),
            "dimension": (ScatterplotDimension,),
            "formula": (str,),
        }

    attribute_map = {
        "alias": "alias",
        "dimension": "dimension",
        "formula": "formula",
    }

    def __init__(self, dimension, formula, *args, **kwargs):
        """
        Formula to be used in a Scatterplot widget query.

        :param alias: Expression alias.
        :type alias: str, optional

        :param dimension: Dimension of the Scatterplot.
        :type dimension: ScatterplotDimension

        :param formula: String expression built from queries, formulas, and functions.
        :type formula: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.dimension = dimension
        self.formula = formula

    @classmethod
    def _from_openapi_data(cls, dimension, formula, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ScatterplotWidgetFormula, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.dimension = dimension
        self.formula = formula
        return self
