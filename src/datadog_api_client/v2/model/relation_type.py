# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RelationType(ModelSimple):
    """
    supported relation types

    :param value: Must be one of ["RelationTypeOwns", "RelationTypeOwnedBy", "RelationTypeDependsOn", "RelationTypeDependencyOf", "RelationTypePartsOf", "RelationTypeHasPart", "RelationTypeOtherOwns", "RelationTypeOtherOwnedBy", "RelationTypeImplementedBy", "RelationTypeImplements"].
    :type value: str
    """

    allowed_values = {
        "RelationTypeOwns",
        "RelationTypeOwnedBy",
        "RelationTypeDependsOn",
        "RelationTypeDependencyOf",
        "RelationTypePartsOf",
        "RelationTypeHasPart",
        "RelationTypeOtherOwns",
        "RelationTypeOtherOwnedBy",
        "RelationTypeImplementedBy",
        "RelationTypeImplements",
    }
    RELATIONTYPEOWNS: ClassVar["RelationType"]
    RELATIONTYPEOWNEDBY: ClassVar["RelationType"]
    RELATIONTYPEDEPENDSON: ClassVar["RelationType"]
    RELATIONTYPEDEPENDENCYOF: ClassVar["RelationType"]
    RELATIONTYPEPARTSOF: ClassVar["RelationType"]
    RELATIONTYPEHASPART: ClassVar["RelationType"]
    RELATIONTYPEOTHEROWNS: ClassVar["RelationType"]
    RELATIONTYPEOTHEROWNEDBY: ClassVar["RelationType"]
    RELATIONTYPEIMPLEMENTEDBY: ClassVar["RelationType"]
    RELATIONTYPEIMPLEMENTS: ClassVar["RelationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RelationType.RELATIONTYPEOWNS = RelationType("RelationTypeOwns")
RelationType.RELATIONTYPEOWNEDBY = RelationType("RelationTypeOwnedBy")
RelationType.RELATIONTYPEDEPENDSON = RelationType("RelationTypeDependsOn")
RelationType.RELATIONTYPEDEPENDENCYOF = RelationType("RelationTypeDependencyOf")
RelationType.RELATIONTYPEPARTSOF = RelationType("RelationTypePartsOf")
RelationType.RELATIONTYPEHASPART = RelationType("RelationTypeHasPart")
RelationType.RELATIONTYPEOTHEROWNS = RelationType("RelationTypeOtherOwns")
RelationType.RELATIONTYPEOTHEROWNEDBY = RelationType("RelationTypeOtherOwnedBy")
RelationType.RELATIONTYPEIMPLEMENTEDBY = RelationType("RelationTypeImplementedBy")
RelationType.RELATIONTYPEIMPLEMENTS = RelationType("RelationTypeImplements")
