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
    from datadog_api_client.v2.model.container_image_flavor import ContainerImageFlavor
    from datadog_api_client.v2.model.container_image_vulnerabilities import ContainerImageVulnerabilities


class ContainerImageAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.container_image_flavor import ContainerImageFlavor
        from datadog_api_client.v2.model.container_image_vulnerabilities import ContainerImageVulnerabilities

        return {
            "container_count": (int,),
            "image_flavors": ([ContainerImageFlavor],),
            "image_tags": ([str],),
            "images_built_at": ([str],),
            "name": (str,),
            "os_architectures": ([str],),
            "os_names": ([str],),
            "os_versions": ([str],),
            "published_at": (str,),
            "registry": (str,),
            "repo_digest": (str,),
            "repository": (str,),
            "short_image": (str,),
            "sizes": ([int],),
            "sources": ([str],),
            "tags": ([str],),
            "vulnerability_count": (ContainerImageVulnerabilities,),
        }

    attribute_map = {
        "container_count": "container_count",
        "image_flavors": "image_flavors",
        "image_tags": "image_tags",
        "images_built_at": "images_built_at",
        "name": "name",
        "os_architectures": "os_architectures",
        "os_names": "os_names",
        "os_versions": "os_versions",
        "published_at": "published_at",
        "registry": "registry",
        "repo_digest": "repo_digest",
        "repository": "repository",
        "short_image": "short_image",
        "sizes": "sizes",
        "sources": "sources",
        "tags": "tags",
        "vulnerability_count": "vulnerability_count",
    }

    def __init__(
        self_,
        container_count: Union[int, UnsetType] = unset,
        image_flavors: Union[List[ContainerImageFlavor], UnsetType] = unset,
        image_tags: Union[List[str], UnsetType] = unset,
        images_built_at: Union[List[str], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        os_architectures: Union[List[str], UnsetType] = unset,
        os_names: Union[List[str], UnsetType] = unset,
        os_versions: Union[List[str], UnsetType] = unset,
        published_at: Union[str, UnsetType] = unset,
        registry: Union[str, UnsetType] = unset,
        repo_digest: Union[str, UnsetType] = unset,
        repository: Union[str, UnsetType] = unset,
        short_image: Union[str, UnsetType] = unset,
        sizes: Union[List[int], UnsetType] = unset,
        sources: Union[List[str], UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        vulnerability_count: Union[ContainerImageVulnerabilities, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for a Container Image.

        :param container_count: Number of containers running the image.
        :type container_count: int, optional

        :param image_flavors: List of platform-specific images associated with the image record.
            The list contains more than 1 entry for multi-architecture images.
        :type image_flavors: [ContainerImageFlavor], optional

        :param image_tags: List of image tags associated with the Container Image.
        :type image_tags: [str], optional

        :param images_built_at: List of build times associated with the Container Image.
            The list contains more than 1 entry for multi-architecture images.
        :type images_built_at: [str], optional

        :param name: Name of the Container Image.
        :type name: str, optional

        :param os_architectures: List of Operating System architectures supported by the Container Image.
        :type os_architectures: [str], optional

        :param os_names: List of Operating System names supported by the Container Image.
        :type os_names: [str], optional

        :param os_versions: List of Operating System versions supported by the Container Image.
        :type os_versions: [str], optional

        :param published_at: Time the image was pushed to the container registry.
        :type published_at: str, optional

        :param registry: Registry the Container Image was pushed to.
        :type registry: str, optional

        :param repo_digest: Digest of the compressed image manifest.
        :type repo_digest: str, optional

        :param repository: Repository where the Container Image is stored in.
        :type repository: str, optional

        :param short_image: Short version of the Container Image name.
        :type short_image: str, optional

        :param sizes: List of size for each platform-specific image associated with the image record.
            The list contains more than 1 entry for multi-architecture images.
        :type sizes: [int], optional

        :param sources: List of sources where the Container Image was collected from.
        :type sources: [str], optional

        :param tags: List of tags associated with the Container Image.
        :type tags: [str], optional

        :param vulnerability_count: Vulnerability counts associated with the Container Image.
        :type vulnerability_count: ContainerImageVulnerabilities, optional
        """
        if container_count is not unset:
            kwargs["container_count"] = container_count
        if image_flavors is not unset:
            kwargs["image_flavors"] = image_flavors
        if image_tags is not unset:
            kwargs["image_tags"] = image_tags
        if images_built_at is not unset:
            kwargs["images_built_at"] = images_built_at
        if name is not unset:
            kwargs["name"] = name
        if os_architectures is not unset:
            kwargs["os_architectures"] = os_architectures
        if os_names is not unset:
            kwargs["os_names"] = os_names
        if os_versions is not unset:
            kwargs["os_versions"] = os_versions
        if published_at is not unset:
            kwargs["published_at"] = published_at
        if registry is not unset:
            kwargs["registry"] = registry
        if repo_digest is not unset:
            kwargs["repo_digest"] = repo_digest
        if repository is not unset:
            kwargs["repository"] = repository
        if short_image is not unset:
            kwargs["short_image"] = short_image
        if sizes is not unset:
            kwargs["sizes"] = sizes
        if sources is not unset:
            kwargs["sources"] = sources
        if tags is not unset:
            kwargs["tags"] = tags
        if vulnerability_count is not unset:
            kwargs["vulnerability_count"] = vulnerability_count
        super().__init__(kwargs)
