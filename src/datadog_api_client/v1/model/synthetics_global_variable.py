# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsGlobalVariable(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_global_variable_attributes import SyntheticsGlobalVariableAttributes
        from datadog_api_client.v1.model.synthetics_global_variable_parse_test_options import (
            SyntheticsGlobalVariableParseTestOptions,
        )
        from datadog_api_client.v1.model.synthetics_global_variable_value import SyntheticsGlobalVariableValue

        return {
            "attributes": (SyntheticsGlobalVariableAttributes,),
            "description": (str,),
            "id": (str,),
            "name": (str,),
            "parse_test_options": (SyntheticsGlobalVariableParseTestOptions,),
            "parse_test_public_id": (str,),
            "tags": ([str],),
            "value": (SyntheticsGlobalVariableValue,),
        }

    attribute_map = {
        "attributes": "attributes",
        "description": "description",
        "id": "id",
        "name": "name",
        "parse_test_options": "parse_test_options",
        "parse_test_public_id": "parse_test_public_id",
        "tags": "tags",
        "value": "value",
    }
    read_only_vars = {
        "id",
    }

    def __init__(self, description, name, tags, value, *args, **kwargs):
        """
        Synthetics global variable.

        :param attributes: Attributes of the global variable.
        :type attributes: SyntheticsGlobalVariableAttributes, optional

        :param description: Description of the global variable.
        :type description: str

        :param id: Unique identifier of the global variable.
        :type id: str, optional

        :param name: Name of the global variable. Unique across Synthetics global variables.
        :type name: str

        :param parse_test_options: Parser options to use for retrieving a Synthetics global variable from a Synthetics Test. Used in conjunction with ``parse_test_public_id``.
        :type parse_test_options: SyntheticsGlobalVariableParseTestOptions, optional

        :param parse_test_public_id: A Synthetic test ID to use as a test to generate the variable value.
        :type parse_test_public_id: str, optional

        :param tags: Tags of the global variable.
        :type tags: [str]

        :param value: Value of the global variable.
        :type value: SyntheticsGlobalVariableValue
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.description = description
        self.name = name
        self.tags = tags
        self.value = value

    @classmethod
    def _from_openapi_data(cls, description, name, tags, value, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsGlobalVariable, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.description = description
        self.name = name
        self.tags = tags
        self.value = value
        return self
