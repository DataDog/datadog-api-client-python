# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SAMLAssertionAttributesType(ModelSimple):
    """
    SAML assertion attributes resource type.

    :param value: If omitted defaults to "saml_assertion_attributes". Must be one of ["saml_assertion_attributes"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "SAML_ASSERTION_ATTRIBUTES": "saml_assertion_attributes",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
