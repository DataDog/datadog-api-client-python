# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class EntityV3(ModelComposed):
    def __init__(self, **kwargs):
        """
        Entity schema v3.

        :param api_version: The schema version of entity type. The field is known as schema-version in the previous version
        :type api_version: EntityV3APIVersion

        :param datadog: Datadog product integrations for the service entity
        :type datadog: EntityV3ServiceDatadog, optional

        :param extensions: Custom extensions. This is the free-formed field to send client side metadata. No Datadog features are affected by this field.
        :type extensions: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param integrations: A base schema for defining third party integrations
        :type integrations: EntityV3Integrations, optional

        :param kind: The definition of Entity V3 Service Kind object.
        :type kind: EntityV3ServiceKind

        :param metadata: The definition of Entity V3 Metadata object.
        :type metadata: EntityV3Metadata

        :param spec: The definition of Entity V3 Service Spec object.
        :type spec: EntityV3ServiceSpec, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.entity_v3_service import EntityV3Service
        from datadog_api_client.v2.model.entity_v3_datastore import EntityV3Datastore
        from datadog_api_client.v2.model.entity_v3_queue import EntityV3Queue
        from datadog_api_client.v2.model.entity_v3_system import EntityV3System

        return {
            "oneOf": [
                EntityV3Service,
                EntityV3Datastore,
                EntityV3Queue,
                EntityV3System,
            ],
        }
