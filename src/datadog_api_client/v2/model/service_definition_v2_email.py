# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ServiceDefinitionV2Email(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_definition_v2_email_type import ServiceDefinitionV2EmailType

        return {
            "contact": (str,),
            "name": (str,),
            "type": (ServiceDefinitionV2EmailType,),
        }

    attribute_map = {
        "contact": "contact",
        "name": "name",
        "type": "type",
    }

    def __init__(self_, contact, type, *args, **kwargs):
        """
        Service owner's email.

        :param contact: Contact value.
        :type contact: str

        :param name: Contact email.
        :type name: str, optional

        :param type: Contact type.
        :type type: ServiceDefinitionV2EmailType
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.contact = contact
        self_.type = type
