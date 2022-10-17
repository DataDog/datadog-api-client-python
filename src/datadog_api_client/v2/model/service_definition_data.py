# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ServiceDefinitionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_definition_data_attributes import ServiceDefinitionDataAttributes

        return {
            "attributes": (ServiceDefinitionDataAttributes,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, *args, **kwargs):
        """
        Service definition data.

        :param attributes: Service definition attributes.
        :type attributes: ServiceDefinitionDataAttributes, optional

        :param type: Service definition type.
        :type type: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
