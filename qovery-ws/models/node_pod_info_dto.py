# coding: utf-8

"""
    websocket-gateway

    Describe the weboscket endpoints

    The version of the OpenAPI document: 0.1.0
    Contact: erebe@erebe.eu
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class NodePodInfoDto(BaseModel):
    """
    NodePodInfoDto
    """ # noqa: E501
    cpu_milli_limit: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    cpu_milli_request: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    environment_id: Optional[StrictStr] = None
    images_version: Dict[str, StrictStr]
    memory_mib_limit: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    memory_mib_request: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    name: StrictStr
    namespace: StrictStr
    project_id: Optional[StrictStr] = None
    service_id: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["cpu_milli_limit", "cpu_milli_request", "environment_id", "images_version", "memory_mib_limit", "memory_mib_request", "name", "namespace", "project_id", "service_id"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NodePodInfoDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if cpu_milli_limit (nullable) is None
        # and model_fields_set contains the field
        if self.cpu_milli_limit is None and "cpu_milli_limit" in self.model_fields_set:
            _dict['cpu_milli_limit'] = None

        # set to None if cpu_milli_request (nullable) is None
        # and model_fields_set contains the field
        if self.cpu_milli_request is None and "cpu_milli_request" in self.model_fields_set:
            _dict['cpu_milli_request'] = None

        # set to None if environment_id (nullable) is None
        # and model_fields_set contains the field
        if self.environment_id is None and "environment_id" in self.model_fields_set:
            _dict['environment_id'] = None

        # set to None if memory_mib_limit (nullable) is None
        # and model_fields_set contains the field
        if self.memory_mib_limit is None and "memory_mib_limit" in self.model_fields_set:
            _dict['memory_mib_limit'] = None

        # set to None if memory_mib_request (nullable) is None
        # and model_fields_set contains the field
        if self.memory_mib_request is None and "memory_mib_request" in self.model_fields_set:
            _dict['memory_mib_request'] = None

        # set to None if project_id (nullable) is None
        # and model_fields_set contains the field
        if self.project_id is None and "project_id" in self.model_fields_set:
            _dict['project_id'] = None

        # set to None if service_id (nullable) is None
        # and model_fields_set contains the field
        if self.service_id is None and "service_id" in self.model_fields_set:
            _dict['service_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of NodePodInfoDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cpu_milli_limit": obj.get("cpu_milli_limit"),
            "cpu_milli_request": obj.get("cpu_milli_request"),
            "environment_id": obj.get("environment_id"),
            "images_version": obj.get("images_version"),
            "memory_mib_limit": obj.get("memory_mib_limit"),
            "memory_mib_request": obj.get("memory_mib_request"),
            "name": obj.get("name"),
            "namespace": obj.get("namespace"),
            "project_id": obj.get("project_id"),
            "service_id": obj.get("service_id")
        })
        return _obj

