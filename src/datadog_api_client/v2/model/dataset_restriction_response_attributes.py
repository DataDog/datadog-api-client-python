# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dataset_restriction_ownership_mode import DatasetRestrictionOwnershipMode
    from datadog_api_client.v2.model.dataset_restriction_restriction_mode import DatasetRestrictionRestrictionMode
    from datadog_api_client.v2.model.dataset_restriction_principal import DatasetRestrictionPrincipal


class DatasetRestrictionResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dataset_restriction_ownership_mode import DatasetRestrictionOwnershipMode
        from datadog_api_client.v2.model.dataset_restriction_restriction_mode import DatasetRestrictionRestrictionMode
        from datadog_api_client.v2.model.dataset_restriction_principal import DatasetRestrictionPrincipal

        return {
            "ownership_mode": (DatasetRestrictionOwnershipMode,),
            "restriction_key": (str,),
            "restriction_mode": (DatasetRestrictionRestrictionMode,),
            "unrestricted_principals": ([DatasetRestrictionPrincipal],),
        }

    attribute_map = {
        "ownership_mode": "ownership_mode",
        "restriction_key": "restriction_key",
        "restriction_mode": "restriction_mode",
        "unrestricted_principals": "unrestricted_principals",
    }

    def __init__(
        self_,
        restriction_mode: DatasetRestrictionRestrictionMode,
        ownership_mode: Union[DatasetRestrictionOwnershipMode, UnsetType] = unset,
        restriction_key: Union[str, UnsetType] = unset,
        unrestricted_principals: Union[List[DatasetRestrictionPrincipal], UnsetType] = unset,
        **kwargs,
    ):
        """
        The current configuration of a dataset restriction, including restriction mode,
        ownership mode, and exempt principals.

        :param ownership_mode: Controls how dataset ownership is determined. ``disabled`` turns off ownership-based access
            entirely. ``team_tag_based`` assigns dataset ownership based on the team tags applied to the
            data, allowing team members to see their own team's datasets.
        :type ownership_mode: DatasetRestrictionOwnershipMode, optional

        :param restriction_key: Internal key used by the restriction enforcement system to identify this restriction rule.
        :type restriction_key: str, optional

        :param restriction_mode: Controls the default data visibility for the product type. ``standard`` makes data visible
            to all users with appropriate product access. ``default_hide`` hides data by default and
            requires explicit grants for each dataset.
        :type restriction_mode: DatasetRestrictionRestrictionMode

        :param unrestricted_principals: Principals (users or roles) that are exempt from this restriction and retain
            full data access regardless of the restriction mode.
        :type unrestricted_principals: [DatasetRestrictionPrincipal], optional
        """
        if ownership_mode is not unset:
            kwargs["ownership_mode"] = ownership_mode
        if restriction_key is not unset:
            kwargs["restriction_key"] = restriction_key
        if unrestricted_principals is not unset:
            kwargs["unrestricted_principals"] = unrestricted_principals
        super().__init__(kwargs)

        self_.restriction_mode = restriction_mode
