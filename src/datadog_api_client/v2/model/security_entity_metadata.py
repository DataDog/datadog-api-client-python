# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SecurityEntityMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "environments": ([str],),
            "mitre_tactics": ([str],),
            "mitre_techniques": ([str],),
            "project_id": (str,),
            "services": ([str],),
            "sources": ([str],),
            "subscription_id": (str,),
        }

    attribute_map = {
        "account_id": "accountID",
        "environments": "environments",
        "mitre_tactics": "mitreTactics",
        "mitre_techniques": "mitreTechniques",
        "project_id": "projectID",
        "services": "services",
        "sources": "sources",
        "subscription_id": "subscriptionID",
    }

    def __init__(
        self_,
        environments: List[str],
        mitre_tactics: List[str],
        mitre_techniques: List[str],
        services: List[str],
        sources: List[str],
        account_id: Union[str, UnsetType] = unset,
        project_id: Union[str, UnsetType] = unset,
        subscription_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata about the entity from cloud providers

        :param account_id: Cloud account ID (AWS)
        :type account_id: str, optional

        :param environments: Environment tags associated with the entity
        :type environments: [str]

        :param mitre_tactics: MITRE ATT&CK tactics detected
        :type mitre_tactics: [str]

        :param mitre_techniques: MITRE ATT&CK techniques detected
        :type mitre_techniques: [str]

        :param project_id: Cloud project ID (GCP)
        :type project_id: str, optional

        :param services: Services associated with the entity
        :type services: [str]

        :param sources: Data sources that detected this entity
        :type sources: [str]

        :param subscription_id: Cloud subscription ID (Azure)
        :type subscription_id: str, optional
        """
        if account_id is not unset:
            kwargs["account_id"] = account_id
        if project_id is not unset:
            kwargs["project_id"] = project_id
        if subscription_id is not unset:
            kwargs["subscription_id"] = subscription_id
        super().__init__(kwargs)

        self_.environments = environments
        self_.mitre_tactics = mitre_tactics
        self_.mitre_techniques = mitre_techniques
        self_.services = services
        self_.sources = sources
