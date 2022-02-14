# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.

from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.nullable_relationship_to_user import NullableRelationshipToUser

    globals()["NullableRelationshipToUser"] = NullableRelationshipToUser


class IncidentCreateRelationships(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "commander_user": (NullableRelationshipToUser,),
        }

    attribute_map = {
        "commander_user": "commander_user",
    }

    read_only_vars = {}

<<<<<<< HEAD
    def __init__(self, commander_user, *args, **kwargs):
        """IncidentCreateRelationships - a model defined in OpenAPI


        :type commander_user: NullableRelationshipToUser
=======
    def __init__(self, commander, *args, **kwargs):
        """
        The relationships the incident will have with other resources once created.

        :param commander: Relationship to user.
        :type commander: RelationshipToUser
>>>>>>> d5bdbdd6e (Use new generator for Python)
        """
        super().__init__(kwargs)

        self._check_pos_args(args)
<<<<<<< HEAD

        self.commander_user = commander_user
=======
        self.commander = commander
>>>>>>> d5bdbdd6e (Use new generator for Python)

    @classmethod
    def _from_openapi_data(cls, commander_user, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentCreateRelationships, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)
<<<<<<< HEAD

        self.commander_user = commander_user
=======
        self.commander = commander

>>>>>>> d5bdbdd6e (Use new generator for Python)
        return self
