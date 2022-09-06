# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsGlobalVariableValue(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "secure": (bool,),
            "value": (str,),
        }

    attribute_map = {
        "secure": "secure",
        "value": "value",
    }

    def __init__(self_, *args, **kwargs):
        """
        Value of the global variable.

        :param secure: Determines if the value of the variable is hidden.
        :type secure: bool, optional

        :param value: Value of the global variable. When reading a global variable,
            the value will not be present if the variable is hidden with the ``secure`` property.
        :type value: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
