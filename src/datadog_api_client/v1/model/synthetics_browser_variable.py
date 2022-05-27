# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsBrowserVariable(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_browser_variable_type import SyntheticsBrowserVariableType

        return {
            "example": (str,),
            "id": (str,),
            "name": (str,),
            "pattern": (str,),
            "type": (SyntheticsBrowserVariableType,),
        }

    attribute_map = {
        "example": "example",
        "id": "id",
        "name": "name",
        "pattern": "pattern",
        "type": "type",
    }

    def __init__(self, name, type, *args, **kwargs):
        """
        Object defining a variable that can be used in your browser test.
        Learn more in the `Browser test Actions documentation <https://docs.datadoghq.com/synthetics/browser_tests/actions#variable>`_.

        :param example: Example for the variable.
        :type example: str, optional

        :param id: ID for the variable. Global variables require an ID.
        :type id: str, optional

        :param name: Name of the variable.
        :type name: str

        :param pattern: Pattern of the variable.
        :type pattern: str, optional

        :param type: Type of browser test variable.
        :type type: SyntheticsBrowserVariableType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.name = name
        self.type = type

    @classmethod
    def _from_openapi_data(cls, name, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsBrowserVariable, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.name = name
        self.type = type
        return self
