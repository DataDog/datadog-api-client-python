# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ApiTypeError,
    ModelSimple,
    cached_property,
)


class AuthNMappingsSort(ModelSimple):

    allowed_values = {
        "value": {
            "CREATED_AT_ASCENDING": "created_at",
            "CREATED_AT_DESCENDING": "-created_at",
            "ROLE_ID_ASCENDING": "role_id",
            "ROLE_ID_DESCENDING": "-role_id",
            "SAML_ASSERTION_ATTRIBUTE_ID_ASCENDING": "saml_assertion_attribute_id",
            "SAML_ASSERTION_ATTRIBUTE_ID_DESCENDING": "-saml_assertion_attribute_id",
            "ROLE_NAME_ASCENDING": "role.name",
            "ROLE_NAME_DESCENDING": "-role.name",
            "SAML_ASSERTION_ATTRIBUTE_KEY_ASCENDING": "saml_assertion_attribute.attribute_key",
            "SAML_ASSERTION_ATTRIBUTE_KEY_DESCENDING": "-saml_assertion_attribute.attribute_key",
            "SAML_ASSERTION_ATTRIBUTE_VALUE_ASCENDING": "saml_assertion_attribute.attribute_value",
            "SAML_ASSERTION_ATTRIBUTE_VALUE_DESCENDING": "-saml_assertion_attribute.attribute_value",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }

    def __init__(self, *args, **kwargs):
        """
        Sorting options for AuthN Mappings.

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: Must be one of ["created_at", "-created_at", "role_id", "-role_id", "saml_assertion_attribute_id", "-saml_assertion_attribute_id", "role.name", "-role.name", "saml_assertion_attribute.attribute_key", "-saml_assertion_attribute.attribute_key", "saml_assertion_attribute.attribute_value", "-saml_assertion_attribute.attribute_value"].
        :type value: str
        """
        super().__init__(kwargs)

        if "value" in kwargs:
            value = kwargs.pop("value")
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=self._path_to_item,
                valid_classes=(self.__class__,),
            )

        self._check_pos_args(args)

        self.value = value

        self._check_kw_args(kwargs)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""
        return cls(*args, **kwargs)
