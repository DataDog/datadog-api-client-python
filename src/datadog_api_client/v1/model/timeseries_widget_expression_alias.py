# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TimeseriesWidgetExpressionAlias(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "alias_name": (str,),
            "expression": (str,),
        }

    attribute_map = {
        "alias_name": "alias_name",
        "expression": "expression",
    }

    def __init__(self, expression, *args, **kwargs):
        """
        Define an expression alias.

        :param alias_name: Expression alias.
        :type alias_name: str, optional

        :param expression: Expression name.
        :type expression: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.expression = expression

    @classmethod
    def _from_openapi_data(cls, expression, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(TimeseriesWidgetExpressionAlias, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.expression = expression
        return self
