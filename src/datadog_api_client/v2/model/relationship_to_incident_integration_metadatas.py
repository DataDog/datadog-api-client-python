# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.relationship_to_incident_integration_metadata_data import (
        RelationshipToIncidentIntegrationMetadataData,
    )

    globals()["RelationshipToIncidentIntegrationMetadataData"] = RelationshipToIncidentIntegrationMetadataData


class RelationshipToIncidentIntegrationMetadatas(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "data": ([RelationshipToIncidentIntegrationMetadataData],),
        }

    attribute_map = {
        "data": "data",
    }

    read_only_vars = {}

    def __init__(self, data, *args, **kwargs):
        """
        A relationship reference for multiple integration metadata objects.

        :param data: The integration metadata relationship array
        :type data: [RelationshipToIncidentIntegrationMetadataData]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.data = data

    @classmethod
    def _from_openapi_data(cls, data, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(RelationshipToIncidentIntegrationMetadatas, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.data = data
        return self
