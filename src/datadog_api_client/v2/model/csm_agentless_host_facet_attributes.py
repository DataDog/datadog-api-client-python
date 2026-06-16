# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CsmAgentlessHostFacetAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "bounded": (bool,),
            "bundled": (bool,),
            "bundled_and_used": (bool,),
            "default_values": ([str],),
            "description": (str,),
            "editable": (bool,),
            "facet_type": (str,),
            "groups": ([str],),
            "name": (str,),
            "path": (str,),
            "source": (str,),
            "type": (str,),
            "values": ([str],),
        }

    attribute_map = {
        "bounded": "bounded",
        "bundled": "bundled",
        "bundled_and_used": "bundledAndUsed",
        "default_values": "defaultValues",
        "description": "description",
        "editable": "editable",
        "facet_type": "facetType",
        "groups": "groups",
        "name": "name",
        "path": "path",
        "source": "source",
        "type": "type",
        "values": "values",
    }

    def __init__(
        self_,
        bounded: bool,
        bundled: bool,
        bundled_and_used: bool,
        default_values: List[str],
        description: str,
        editable: bool,
        facet_type: str,
        groups: List[str],
        name: str,
        path: str,
        source: str,
        type: str,
        values: List[str],
        **kwargs,
    ):
        """
        Attributes of an agentless host facet.

        :param bounded: Whether the facet has a bounded set of allowed values. ``true`` indicates a fixed value set and ``false`` indicates free-form values.
        :type bounded: bool

        :param bundled: Whether the facet is bundled as part of the default facet set. ``true`` indicates bundled and ``false`` indicates custom.
        :type bundled: bool

        :param bundled_and_used: Whether the facet is both bundled and actively used. ``true`` indicates in use; ``false`` indicates unused.
        :type bundled_and_used: bool

        :param default_values: The list of default filter values for the facet.
        :type default_values: [str]

        :param description: A human-readable description of what the facet represents.
        :type description: str

        :param editable: Whether the facet can be edited by users. ``true`` indicates editable; ``false`` indicates read-only.
        :type editable: bool

        :param facet_type: The UI display type for the facet, such as ``list``.
        :type facet_type: str

        :param groups: The list of UI groups that this facet belongs to.
        :type groups: [str]

        :param name: The display name of the facet.
        :type name: str

        :param path: The field path used when filtering by this facet.
        :type path: str

        :param source: The data source that provides the facet values.
        :type source: str

        :param type: The data type of the facet values.
        :type type: str

        :param values: The list of allowed filter values for bounded facets. Empty for unbounded facets.
        :type values: [str]
        """
        super().__init__(kwargs)

        self_.bounded = bounded
        self_.bundled = bundled
        self_.bundled_and_used = bundled_and_used
        self_.default_values = default_values
        self_.description = description
        self_.editable = editable
        self_.facet_type = facet_type
        self_.groups = groups
        self_.name = name
        self_.path = path
        self_.source = source
        self_.type = type
        self_.values = values
