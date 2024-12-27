# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.advisory import Advisory


class Remediation(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.advisory import Advisory

        return {
            "auto_solvable": (bool,),
            "avoided_advisories": ([Advisory],),
            "fixed_advisories": ([Advisory],),
            "library_name": (str,),
            "library_version": (str,),
            "new_advisories": ([Advisory],),
            "remaining_advisories": ([Advisory],),
            "type": (str,),
        }

    attribute_map = {
        "auto_solvable": "auto_solvable",
        "avoided_advisories": "avoided_advisories",
        "fixed_advisories": "fixed_advisories",
        "library_name": "library_name",
        "library_version": "library_version",
        "new_advisories": "new_advisories",
        "remaining_advisories": "remaining_advisories",
        "type": "type",
    }

    def __init__(
        self_,
        auto_solvable: bool,
        avoided_advisories: List[Advisory],
        fixed_advisories: List[Advisory],
        library_name: str,
        library_version: str,
        new_advisories: List[Advisory],
        remaining_advisories: List[Advisory],
        type: str,
        **kwargs,
    ):
        """
        Vulnerability remediation.

        :param auto_solvable: Whether the vulnerability can be resolved when recompiling the package or not.
        :type auto_solvable: bool

        :param avoided_advisories: Avoided advisories.
        :type avoided_advisories: [Advisory]

        :param fixed_advisories: Remediation fixed advisories.
        :type fixed_advisories: [Advisory]

        :param library_name: Library name remediating the vulnerability.
        :type library_name: str

        :param library_version: Library version remediating the vulnerability.
        :type library_version: str

        :param new_advisories: New advisories.
        :type new_advisories: [Advisory]

        :param remaining_advisories: Remaining advisories.
        :type remaining_advisories: [Advisory]

        :param type: Remediation type.
        :type type: str
        """
        super().__init__(kwargs)

        self_.auto_solvable = auto_solvable
        self_.avoided_advisories = avoided_advisories
        self_.fixed_advisories = fixed_advisories
        self_.library_name = library_name
        self_.library_version = library_version
        self_.new_advisories = new_advisories
        self_.remaining_advisories = remaining_advisories
        self_.type = type
