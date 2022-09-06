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

    def __init__(self_, expression, *args, **kwargs):
        """
        Define an expression alias.

        :param alias_name: Expression alias.
        :type alias_name: str, optional

        :param expression: Expression name.
        :type expression: str
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.expression = expression
