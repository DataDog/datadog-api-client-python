# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.sca_request_data_attributes_commit import ScaRequestDataAttributesCommit
    from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items import (
        ScaRequestDataAttributesDependenciesItems,
    )
    from datadog_api_client.v2.model.sca_request_data_attributes_files_items import ScaRequestDataAttributesFilesItems
    from datadog_api_client.v2.model.sca_request_data_attributes_relations_items import (
        ScaRequestDataAttributesRelationsItems,
    )
    from datadog_api_client.v2.model.sca_request_data_attributes_repository import ScaRequestDataAttributesRepository
    from datadog_api_client.v2.model.sca_request_data_attributes_vulnerabilities_items import (
        ScaRequestDataAttributesVulnerabilitiesItems,
    )


class ScaRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sca_request_data_attributes_commit import ScaRequestDataAttributesCommit
        from datadog_api_client.v2.model.sca_request_data_attributes_dependencies_items import (
            ScaRequestDataAttributesDependenciesItems,
        )
        from datadog_api_client.v2.model.sca_request_data_attributes_files_items import (
            ScaRequestDataAttributesFilesItems,
        )
        from datadog_api_client.v2.model.sca_request_data_attributes_relations_items import (
            ScaRequestDataAttributesRelationsItems,
        )
        from datadog_api_client.v2.model.sca_request_data_attributes_repository import (
            ScaRequestDataAttributesRepository,
        )
        from datadog_api_client.v2.model.sca_request_data_attributes_vulnerabilities_items import (
            ScaRequestDataAttributesVulnerabilitiesItems,
        )

        return {
            "commit": (ScaRequestDataAttributesCommit,),
            "dependencies": ([ScaRequestDataAttributesDependenciesItems],),
            "env": (str,),
            "files": ([ScaRequestDataAttributesFilesItems],),
            "relations": ([ScaRequestDataAttributesRelationsItems],),
            "repository": (ScaRequestDataAttributesRepository,),
            "service": (str,),
            "tags": ({str: (str,)},),
            "vulnerabilities": ([ScaRequestDataAttributesVulnerabilitiesItems],),
        }

    attribute_map = {
        "commit": "commit",
        "dependencies": "dependencies",
        "env": "env",
        "files": "files",
        "relations": "relations",
        "repository": "repository",
        "service": "service",
        "tags": "tags",
        "vulnerabilities": "vulnerabilities",
    }

    def __init__(
        self_,
        commit: Union[ScaRequestDataAttributesCommit, UnsetType] = unset,
        dependencies: Union[List[ScaRequestDataAttributesDependenciesItems], UnsetType] = unset,
        env: Union[str, UnsetType] = unset,
        files: Union[List[ScaRequestDataAttributesFilesItems], UnsetType] = unset,
        relations: Union[List[ScaRequestDataAttributesRelationsItems], UnsetType] = unset,
        repository: Union[ScaRequestDataAttributesRepository, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        tags: Union[Dict[str, str], UnsetType] = unset,
        vulnerabilities: Union[List[ScaRequestDataAttributesVulnerabilitiesItems], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param commit:
        :type commit: ScaRequestDataAttributesCommit, optional

        :param dependencies:
        :type dependencies: [ScaRequestDataAttributesDependenciesItems], optional

        :param env:
        :type env: str, optional

        :param files:
        :type files: [ScaRequestDataAttributesFilesItems], optional

        :param relations:
        :type relations: [ScaRequestDataAttributesRelationsItems], optional

        :param repository:
        :type repository: ScaRequestDataAttributesRepository, optional

        :param service:
        :type service: str, optional

        :param tags:
        :type tags: {str: (str,)}, optional

        :param vulnerabilities:
        :type vulnerabilities: [ScaRequestDataAttributesVulnerabilitiesItems], optional
        """
        if commit is not unset:
            kwargs["commit"] = commit
        if dependencies is not unset:
            kwargs["dependencies"] = dependencies
        if env is not unset:
            kwargs["env"] = env
        if files is not unset:
            kwargs["files"] = files
        if relations is not unset:
            kwargs["relations"] = relations
        if repository is not unset:
            kwargs["repository"] = repository
        if service is not unset:
            kwargs["service"] = service
        if tags is not unset:
            kwargs["tags"] = tags
        if vulnerabilities is not unset:
            kwargs["vulnerabilities"] = vulnerabilities
        super().__init__(kwargs)
